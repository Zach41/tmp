#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from collections import defaultdict

vocabularies = []
with open("vocabularies.txt", 'r') as fr:
    vocabularies = json.load(fr)


def _read_dir(dirname, out_file, word_sz):
    print "IN %s" % dirname
    file_vecs = []
    for filename in os.listdir(dirname):
        if not filename.endswith("opseq"):
            continue
        print "\tProcessing %s" % filename
        file_vec = [0] * len(vocabularies)
        word_cnt = defaultdict(int)
        total_word_cnt = 0
        file_str = []
        with open(os.path.join(dirname, filename), 'r') as fr:
            lines = fr.readlines()
            for line in lines:
                file_str.append(line.strip())
        file_str = ''.join(file_str)
        for i in range(0, len(file_str) - word_sz, word_sz):
            word_cnt[file_str[i:i + word_sz]] += 1
        for i in range(len(vocabularies)):
            if vocabularies[i] in word_cnt:
                total_word_cnt += word_cnt[vocabularies[i]]
                # file_vec[i] = float(word_cnt[vocabularies[i]]) / float(
                #     total_word_cnt)
                file_vec[i] = 1
        file_vecs.append(file_vec)
    with open(out_file, "w") as fw:
        json.dump(file_vecs, fw)


_read_dir("malwares_opseq", "neural_vec_malwares.txt", 10)
_read_dir("benign_opseq", "neural_vec_benigns.txt", 10)
