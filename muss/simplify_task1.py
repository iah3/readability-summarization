# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import argparse
from nltk.tokenize import sent_tokenize
from tqdm import tqdm


from muss.simplify import ALLOWED_MODEL_NAMES, simplify_sentences
from muss.utils.helpers import read_lines


if __name__ == '__main__':
    model_name = 'muss_en_wikilarge_mined'

    filess = ['../task1/bart/test/plos.txt',
              '../task1/bart/test/elife.txt',
              '../task1/bart/val/elife.txt',
              '../task1/bart/val/plos.txt']

    for file in filess:
        simplified_sentences = []
        with open(file, encoding='utf-8') as file_read:
            source_sentences = file_read.readlines()
        for line in tqdm(source_sentences):
            simplified_sentences.append(simplify_sentences(sent_tokenize(line), model_name=model_name))
        with open(file.replace('bart', 'bart/muss'), "w") as f:
            for summary in simplified_sentences:
                f.write(' '.join(summary) + "\n")