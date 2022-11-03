from random import shuffle
import json
import csv
import re


if __name__ == '__main__':
  content = []
  with open('data/hcpa_covid_binary.csv', 'r') as text_file:
    csv_file = csv.reader(text_file)
    next(csv_file)
    for line in csv_file:
      text_norm = re.sub(r'[\n]+', '', line[6])
      content.append([text_norm, line[8]])

  binary_cl_json = json.load(open('data/binary_566.json', 'r'))
  for item in binary_cl_json:
    text_norm = re.sub(r'[\n]+', '', item['text'])
    content.append([text_norm, item['covid-cl']])

  shuffle(content)

  csv_final = csv.writer(open('data/opas_covidcl_ds.csv', 'w'))
  csv_final.writerow(['sent', 'cl'])
  for c in content:
    csv_final.writerow([c[0], c[1]])
