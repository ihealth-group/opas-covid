from wasabi import Printer
from pathlib import Path
import tarfile
import typer
import os

msg = Printer()


def main(model_name: str, dest: Path):
  msg.info(f"unpacking {model_name}")
  tar = tarfile.open(f'{model_name}')
  tar.extractall(dest)
  tar.close()
  msg.info("removing old tar file...")
  os.remove(model_name)


if __name__ == "__main__":
  typer.run(main)
