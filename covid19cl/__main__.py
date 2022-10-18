from transformers.training_args import HubStrategy
from transformers import (
  AutoModelForSequenceClassification,
  DataCollatorWithPadding,
  EarlyStoppingCallback,
  XLMRobertaTokenizerFast,
  TrainingArguments,
  IntervalStrategy,
  set_seed
)
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report
from covid19cl.run_params import OpasCovidParams
from .unbalanced import UnbalancedTrainer
from covid19cl.loadds import load_ds
import numpy as np
import evaluate
import wandb


if __name__ == '__main__':
  args = OpasCovidParams().get_params()
  w_run = wandb.init(project=args.wandb_project_id, entity=args.wandb_entity)
  set_seed(42)

  accuracy_metric = evaluate.load("accuracy")
  f1_metric = evaluate.load("f1")
  precision_metric = evaluate.load("precision")
  recall_metric = evaluate.load("recall")

  dataset = load_ds(
    ds_id=args.corpus_id,
    root_bucket=args.root_bucket,
    text_cl_positions=args.text_cl_positions
  )

  sent_feature = dataset["train"].features["label"]
  label_names = sent_feature.names

  id2label = {str(i): label for i, label in enumerate(label_names)}
  label2id = {v: k for k, v in id2label.items()}

  cl_labels = dataset['train']['label']
  classes = np.unique(cl_labels)
  weights = compute_class_weight('balanced', classes=classes, y=cl_labels)


  def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)

    perclass_report = classification_report(
      predictions,
      labels,
      target_names=label_names,
      output_dict=True,
      zero_division=0
    )
    for label_report in perclass_report:
      if label_report in label_names:
        w_run.log({f'precision_{label_report}': perclass_report[label_report]['precision']})
        w_run.log({f'recall_{label_report}': perclass_report[label_report]['recall']})
        w_run.log({f'f1_{label_report}': perclass_report[label_report]['f1-score']})
        w_run.log({f'support_{label_report}': perclass_report[label_report]['support']})

    accuracy_overall = accuracy_metric.compute(predictions=predictions, references=labels)
    f1_overall = f1_metric.compute(predictions=predictions, references=labels, average='weighted')
    precision_overall = precision_metric.compute(predictions=predictions, references=labels, average='weighted')
    recall_overall = recall_metric.compute(predictions=predictions, references=labels, average='weighted')

    w_run.log(accuracy_overall)
    w_run.log(f1_overall)
    w_run.log(precision_overall)
    w_run.log(recall_overall)

    return f1_overall


  tokenizer = XLMRobertaTokenizerFast.from_pretrained(args.lm, add_prefix_space=True, use_auth_token=True)


  def preprocess_function(examples):
    return tokenizer(examples["sentence"], truncation=True)


  tokenized_datasets = dataset.map(preprocess_function, batched=True)
  data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

  model = AutoModelForSequenceClassification.from_pretrained(
    args.lm,
    num_labels=len(label_names),
    id2label=id2label,
    label2id=label2id,
    use_auth_token=True
  )

  args_training = TrainingArguments(
    num_train_epochs=300,
    per_device_train_batch_size=64,
    gradient_accumulation_steps=1,
    load_best_model_at_end=True,
    evaluation_strategy=IntervalStrategy.STEPS,
    metric_for_best_model='f1',
    gradient_checkpointing=True,
    save_total_limit=1,
    warmup_steps=100,
    weight_decay=0.01,
    learning_rate=2e-5,
    report_to=["wandb"],
    logging_steps=100,
    do_eval=True,
    fp16=True,
    push_to_hub=True,
    hub_strategy=HubStrategy.END,
    hub_model_id=args.hub_model_id,
    output_dir=args.output_dir,
    overwrite_output_dir=True
  )

  trainer = UnbalancedTrainer(
    model=model,
    args=args_training,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=10)],
    weights=weights.tolist()
  )

  trainer.train()
  trainer.save_model()
  w_run.finish()
