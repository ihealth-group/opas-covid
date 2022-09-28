from covid19cl.trainer import run_cl_training
from covid19cl.loadds import load_ds
from wasabi import Printer
from pathlib import Path
import tarfile
import boto3
import tqdm
import os

LM_NAME = 'shc-lm-v3.1'
MODEL_NAME = 'covid19-cl-v1.5.0-lmv3.1'
ROOT_BUCKET = os.environ.get('BUCKET_DS', 'opas-oms')
msg = Printer()


def main():
  os.makedirs('assets', exist_ok=True)
  model_dir = Path('assets') / LM_NAME
  # model_dir = LM_NAME

  s3 = boto3.client('s3')
  if not model_dir.exists():
    msg.info(f'downloading {LM_NAME}')
    kwargs = {"Bucket": 'shc-ai-models', "Key": f'language_model/{LM_NAME}.tar.gz'}
    object_size = s3.head_object(**kwargs)["ContentLength"]
    with tqdm.tqdm(total=object_size, unit="B", unit_scale=True, desc=LM_NAME) as pbar:
      s3.download_file(
        'shc-ai-models',
        f'language_model/{LM_NAME}.tar.gz',
        f'{str(model_dir)}.tar.gz',
        Callback=lambda bytes_transferred: pbar.update(bytes_transferred)
      )

      msg.info('unpaking model...')
      tar = tarfile.open(f'{str(model_dir)}.tar.gz')
      tar.extractall(Path('assets'))
      tar.close()

  dataset = load_ds(ds_id='cns_hcpa.csv')

  finalmodel_path = Path('assets') / MODEL_NAME

  run_cl_training(
    dataset=dataset,
    model_name=Path(model_dir),
    output_dir=finalmodel_path
  )

  msg.info('archiving model...')
  archive = tarfile.open(f"{MODEL_NAME}.tar.gz", "w|gz")
  archive.add(finalmodel_path, arcname=MODEL_NAME)
  archive.close()

  msg.info('uploading model...')
  s3.upload_file(f'{MODEL_NAME}.tar.gz', 'opas-oms', f'{MODEL_NAME}.tar.gz')

  msg.info("that's all folks!")


if __name__ == "__main__":
  main()
