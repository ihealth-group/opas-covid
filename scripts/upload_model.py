from wasabi import Printer
import typer
import boto3

msg = Printer()

aws_s3 = boto3.client('s3')


def main(trained_model_path: str, bucket_name: str, bucket_filename):
  msg.info(f'commencing upload of {trained_model_path} to {bucket_name}')
  aws_s3.upload_file(trained_model_path, bucket_name, bucket_filename)
  msg.info('upload complete')


if __name__ == "__main__":
  typer.run(main)
