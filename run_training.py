from covid19cl.run_params import OpasCovidParams
from covid19cl.trainer import run_cl_training
from covid19cl.loadds import load_ds
from wasabi import Printer
from pathlib import Path
import tarfile
import boto3
import tqdm
import os

msg = Printer()


def main():
  args = OpasCovidParams().get_params()
  os.makedirs('assets', exist_ok=True)
  model_dir = Path('assets') / args.lm

  s3 = boto3.client('s3')
  if not model_dir.exists():
    msg.info(f'downloading {args.lm}')
    kwargs = {"Bucket": 'shc-ai-models', "Key": f'language_model/{args.lm}.tar.gz'}
    object_size = s3.head_object(**kwargs)["ContentLength"]
    with tqdm.tqdm(total=object_size, unit="B", unit_scale=True, desc=args.lm) as pbar:
      s3.download_file(
        args.lm_bucket,
        f'language_model/{args.lm}.tar.gz',
        f'{str(model_dir)}.tar.gz',
        Callback=lambda bytes_transferred: pbar.update(bytes_transferred)
      )

      msg.info('unpaking model...')
      tar = tarfile.open(f'{str(model_dir)}.tar.gz')
      tar.extractall(Path('assets'))
      tar.close()

  dataset = load_ds(
    ds_id=args.corpus_id,
    root_bucket=args.root_bucket,
    text_cl_positions=args.text_cl_positions
  )

  finalmodel_path = Path('assets') / args.model_name

  run_cl_training(
    dataset=dataset,
    model_name=Path(model_dir),
    output_dir=finalmodel_path
  )

  msg.info("that's all folks!")


if __name__ == "__main__":
  main()
