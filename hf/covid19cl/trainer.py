from transformers import (
  AutoModelForSequenceClassification,
  DataCollatorWithPadding,
  EarlyStoppingCallback,
  TrainingArguments,
  IntervalStrategy,
  set_seed
)
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report
from transformers import RobertaTokenizerFast
from .unbalanced import UnbalancedTrainer
import numpy as np
import evaluate
import wandb


def run_cl_training(dataset, model_name, output_dir):
  w_run = wandb.init(project='opas-oms', entity="ihealth", notes="Covid19 Classifier")
  set_seed(42)

  accuracy_metric = evaluate.load("accuracy")
  f1_metric = evaluate.load("f1")
  precision_metric = evaluate.load("precision")
  recall_metric = evaluate.load("recall")

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

  tokenizer = RobertaTokenizerFast.from_pretrained(model_name, add_prefix_space=True)

  def preprocess_function(examples):
    return tokenizer(examples["sentence"], truncation=True)

  tokenized_datasets = dataset.map(preprocess_function, batched=True)
  data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

  model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=len(label_names),
    id2label=id2label,
    label2id=label2id
  )

  args = TrainingArguments(
    model_name,
    overwrite_output_dir=True,
    num_train_epochs=200,
    per_device_train_batch_size=64,
    gradient_accumulation_steps=1,
    load_best_model_at_end=True,
    evaluation_strategy=IntervalStrategy.EPOCH,
    save_strategy=IntervalStrategy.EPOCH,
    metric_for_best_model='f1',
    gradient_checkpointing=True,
    optim="adafactor",
    save_total_limit=1,
    warmup_steps=20,
    weight_decay=0.01,
    learning_rate=2e-5,
    report_to=["wandb"],
    logging_steps=20,
    do_eval=True,
    fp16=True
  )

  trainer = UnbalancedTrainer(
    model=model,
    args=args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=10)],
    weights=weights.tolist()
  )

  trainer.train()
  trainer.save_model(output_dir=output_dir)
  w_run.finish()
