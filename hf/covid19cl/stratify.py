from collections import Counter
import math
import csv


def stratify_text_cl(corpus, perc: float, skip_header: bool = True, train_path=None, eval_path=None):
  counter = Counter()
  with open(corpus, 'r') as corpus_file:
    csvreader = csv.reader(corpus_file, delimiter=",")
    if skip_header:
      next(csvreader)
    for line in csvreader:
      counter.update({line[8]: 1})

  classes_count = sorted(counter.items(), key=lambda pair: pair[1], reverse=False)
  classes_dev_count = [(cl[0], math.floor(cl[1] * perc)) for cl in classes_count]
  train_file = open(train_path, 'a')
  eval_file = open(eval_path, 'a')

  train_file.write("sentence,class\n")
  eval_file.write("sentence,class\n")

  with open(corpus, 'r') as corpus_file:
    csvreader = csv.reader(corpus_file, delimiter=",")
    if skip_header:
      next(csvreader)
      for line in csvreader:
        classes_dev_count_pair = [(pair, idx) for idx, pair in enumerate(classes_dev_count) if pair[0] == line[8]][0]
        if classes_dev_count_pair[0][1] > 0:
          eval_file.write(f'"{line[6]}",{line[8]}\n')
          del classes_dev_count[classes_dev_count_pair[1]]
          classes_dev_count_pair = (classes_dev_count_pair[0][0], classes_dev_count_pair[0][1] - 1)
          classes_dev_count.append(classes_dev_count_pair)
        else:
          train_file.write(f'"{line[6]}",{line[8]}\n')

      train_file.close()
      eval_file.close()
