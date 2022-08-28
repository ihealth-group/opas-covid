from spacy.tokens import DocBin
from collections import Counter
from wasabi import Printer
from pathlib import Path
import typer
import spacy
import math

msg = Printer()


def main(corpus: Path, train: Path, dev: Path):
  nlp = spacy.blank("en")
  msg.info('creating blank nlp object')
  doc_bin = DocBin().from_disk(corpus)
  msg.info('docs loaded from disk')
  docs_from_bin = doc_bin.get_docs(nlp.vocab)
  docs = []
  counter = Counter()
  docbin_train = DocBin()
  docbin_dev = DocBin()

  for doc in docs_from_bin:
    label = list(doc.cats.keys())[list(doc.cats.values()).index(1)]
    if label != '':
      docs.append(doc)
      counter.update({label: 1})

  msg.info('counter updated with ents count. result:')
  classes_count = sorted(counter.items(), key=lambda pair: pair[1], reverse=False)
  msg.info(classes_count)

  classes_dev_count = [(cl[0], math.floor(cl[1] * .2)) for cl in classes_count]
  msg.info('dev counter updated:')
  msg.info(classes_dev_count)

  docs_train = []
  docs_dev = []
  msg.info('commencing stratification')
  for doc in docs:
    label = list(doc.cats.keys())[list(doc.cats.values()).index(1)]
    classes_dev_count_pair = [(pair, idx) for idx, pair in enumerate(classes_dev_count) if pair[0] == label][0]
    if classes_dev_count_pair[0][1] > 0:
      docs_dev.append(doc)
      del classes_dev_count[classes_dev_count_pair[1]]
      classes_dev_count_pair = (classes_dev_count_pair[0][0], classes_dev_count_pair[0][1] - 1)
      classes_dev_count.append(classes_dev_count_pair)

  seen_in_devset = set([doc.text for doc in docs_dev])
  for doc in docs:
    if doc.text not in seen_in_devset:
      docs_train.append(doc)

  for doc in docs_train:
    docbin_train.add(doc)
  for doc in docs_dev:
    docbin_dev.add(doc)

  docbin_train.to_disk(train)
  msg.info('train set generated')
  docbin_dev.to_disk(dev)
  msg.info('dev set generated')


if __name__ == "__main__":
  typer.run(main)
