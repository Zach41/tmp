#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import os
# import operator
# import json

print "Generating Features Dictionary"

rec = defaultdict(int)
OPSEQ_LEN = int(os.environ.get("OPSEQ_LEN", 10))

M_TRAININGSET_PATH = os.path.join("malwares_opseq", "training_set")
B_TRAININGSET_PATH = os.path.join("benign_opseq", "training_set")

for filename in os.listdir(M_TRAININGSET_PATH):
    if not filename.endswith("opseq"):
        continue
    filename = os.path.join(M_TRAININGSET_PATH, filename)
    print "processing %s" % filename
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        tmp = []
        for line in lines:
            tmp.append(line[:-1])
        file_str = ''.join(tmp)

        for i in range(0, len(file_str) - OPSEQ_LEN):
            rec[file_str[i:i + OPSEQ_LEN]] += 1

for filename in os.listdir(B_TRAININGSET_PATH):
    if not filename.endswith("opseq"):
        continue
    filename = os.path.join(B_TRAININGSET_PATH, filename)
    print "processing %s" % filename
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        tmp = []
        for line in lines:
            tmp.append(line[:-1])
        file_str = ''.join(tmp)

        for i in range(0, len(file_str) - OPSEQ_LEN):
            rec[file_str[i:i + OPSEQ_LEN]] += 1

print "\n\nUNIQUE OP-VEC NUMBER: %d" % len(rec.keys())
