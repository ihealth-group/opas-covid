import argparse


class OpasCovidParams:
  def __init__(self):
    parser = argparse.ArgumentParser(description='Opas Covid')
    parser.add_argument('--lm', default="shc-lm-v3.1", type=str)
    parser.add_argument('--model_name', default="covid19-uti-cl-v1.0.0-lmv3.1", type=str)
    parser.add_argument('--root_bucket', default="opas-oms", type=str)
    parser.add_argument('--lm_bucket', default="shc-ai-models", type=str)
    parser.add_argument('--corpus_id', default="cns_hcpa.csv", type=str)
    parser.add_argument('--text_cl_positions', default="1,2", type=str)

    self.opts = parser.parse_args()

  def get_params(self):
    return self.opts
