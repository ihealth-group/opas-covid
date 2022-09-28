from transformers import Trainer
from torch import nn
import torch


class UnbalancedTrainer(Trainer):

  def __init__(self, *args, weights, **kwargs):
    cuda0 = torch.device('cuda:0')
    self._weights = torch.tensor(weights).to(cuda0)
    super(UnbalancedTrainer, self).__init__(*args, **kwargs)

  def compute_loss(self, model, inputs, return_outputs=False):
    labels = inputs.get("labels")
    # forward pass
    outputs = model(**inputs)
    logits = outputs.get('logits')
    # compute custom loss
    loss_fct = nn.CrossEntropyLoss(weight=self._weights)
    loss = loss_fct(logits.view(-1, model.config.num_labels), labels.view(-1))
    return (loss, outputs) if return_outputs else loss
