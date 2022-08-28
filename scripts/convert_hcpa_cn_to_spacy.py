from spacy.tokens import DocBin
from wasabi import Printer
import spacy

from pathlib import Path
import typer
import csv

msg = Printer()


def generate_examples(nlp, file: Path):
  docs = DocBin()
  cats = {'NOT_COVID': 0, 'SRAG_moderado': 0, 'SRAG_Severo': 0, 'COVID_assint_leve': 0}
  with file.open("r", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
      text = row[6]
      clazz = row[8]
      if clazz == 'QUESTIONAVEL':
        continue

      if len(text) > 510:
        text = text[: 255] + text[-255:]

      doc = nlp.make_doc(text)
      doc_class = cats.copy()
      doc_class[clazz] = 1
      doc.cats = doc_class
      docs.add(doc)
  return docs


def main(corpus_pristine: Path, corpus_spacy: Path):
  msg.info('creating nlp object')
  nlp = spacy.blank('en')

  msg.info('loading sentences')
  train_docs = generate_examples(nlp, corpus_pristine)

  msg.info('saving spacy file')
  train_docs.to_disk(corpus_spacy)


if __name__ == "__main__":
  typer.run(main)

