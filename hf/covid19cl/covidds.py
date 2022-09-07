import datasets
import csv


class Covid19CLConfig(datasets.BuilderConfig):
  def __init__(self, **kwargs):
    super(Covid19CLConfig, self).__init__(**kwargs)


class Covid19CL(datasets.GeneratorBasedBuilder):
  BUILDER_CONFIGS = [
    Covid19CLConfig(
      name="Covid19CL",
      version=datasets.Version("1.0.0"),
      description="Annottated COVID 19's clinical notes"
    )
  ]

  def __init__(self,
               *args,
               cache_dir,
               train_file="train.ds",
               eval_file="eval.ds",
               classes=None,
               **kwargs):
    self._classes = classes
    self._train_file = train_file
    self._eval_file = eval_file
    super(Covid19CL, self).__init__(*args, cache_dir=cache_dir, **kwargs)

  def _info(self):
    return datasets.DatasetInfo(
      description="COVID 19 dataset",
      features=datasets.Features(
        {
          "id": datasets.Value("string"),
          "sentence": datasets.Value("string"),
          "label": datasets.features.ClassLabel(
              names=sorted(list(self._classes))
            )
        }
      ),
      supervised_keys=None,
      homepage="https://www.ihealthgroup.com.br",
      citation="",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    return [
      datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": self._train_file}),
      datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": self._eval_file})
    ]

  def _generate_examples(self, filepath):
    with open(filepath, encoding="utf-8") as f:
      csvreader = csv.reader(f, delimiter=",")
      next(csvreader)
      for guid, line in enumerate(csvreader):
        yield guid, {
          "id": str(guid),
          "sentence": line[6],
          "label": line[8]
        }
