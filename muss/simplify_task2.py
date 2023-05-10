# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
from datasets import load_dataset
import argparse
from nltk.tokenize import sent_tokenize
from tqdm import tqdm


from muss.simplify import ALLOWED_MODEL_NAMES, simplify_sentences
from muss.utils.helpers import read_lines
import os

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

if __name__ == '__main__':
    filess = ['../task2/lsg/abstract.txt']
    # print(filess)
    model_name = 'muss_en_wikilarge_mined'
    
    for file in filess:
        simplified_sentences = []
        with open(file, encoding='utf-8') as file_read:
            source_sentences = file_read.readlines()
        for line in tqdm(source_sentences):
            # print(line, '\n\n\n', sent_tokenize(line))
            simplified_sentences.append(simplify_sentences(sent_tokenize(line), model_name=model_name))
            # print(' '.join(simplified_sentences[-1]))
        with open(file.replace('abstract', 'laysumm'), "w") as f:
            for summary in simplified_sentences:
                f.write(' '.join(summary) + "\n")