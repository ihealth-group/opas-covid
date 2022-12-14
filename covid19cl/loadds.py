from .stratify import stratify_text_cl
from .covidds import Covid19CL
from wasabi import Printer
from pathlib import Path
import boto3
import tqdm
import csv
import os

WORKING_DIR = os.environ.get('WORKING_DIR', '.working')

s3 = boto3.client('s3')

msg = Printer()


def load_ds(ds_id: str, root_bucket: str, text_cl_positions: str):
  splits_cl_pos = text_cl_positions.split(',')
  text_pos = int(splits_cl_pos[0])
  cl_pos = int(splits_cl_pos[1])
  os.makedirs(WORKING_DIR, exist_ok=True)
  ds = WORKING_DIR / Path(ds_id)
  if not ds.exists():
    msg.info(f'downloading {ds_id}')
    kwargs = {"Bucket": root_bucket, "Key": ds_id}
    object_size = s3.head_object(**kwargs)["ContentLength"]
    with tqdm.tqdm(total=object_size, unit="B", unit_scale=True, desc=ds_id) as pbar:
      s3.download_file(
        root_bucket,
        ds_id,
        str(ds),
        Callback=lambda bytes_transferred: pbar.update(bytes_transferred)
      )
  msg.info('preparing dataset...')
  classes = set()
  msg.info('detecting available classes')
  with open(ds, 'r') as dataset:
    csvreader = csv.reader(dataset, delimiter=",")
    next(csvreader)
    for line in csvreader:
      classes.add(line[cl_pos])

  # msg.pretty(classes)

  train_file = Path(f'{WORKING_DIR}/train.ds')
  eval_file = Path(f'{WORKING_DIR}/eval.ds')

  if not train_file.exists():
    stratify_text_cl(
      corpus=ds,
      perc=.2,
      train_path=train_file,
      eval_path=eval_file,
      text_pos=text_pos,
      cl_pos=cl_pos
    )

  dataset = Covid19CL(
    cache_dir=WORKING_DIR,
    train_file=train_file,
    eval_file=eval_file,
    classes=tuple(list(classes))
  )

  dataset.download_and_prepare()
  msg.info('returning dataset')
  return dataset.as_dataset()
