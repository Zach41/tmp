#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import os
import operator
import json

print "Generating Features Dictionary"

rec = defaultdict(int)
OPSEQ_LEN = int(os.environ.get("OPSEQ_LEN", 10))

TRAININGSET_PATH = os.path.join("malwares_opseq", "training_set")

for filename in os.listdir(TRAININGSET_PATH):
    if not filename.endswith("opseq"):
        continue
    filename = os.path.join(TRAININGSET_PATH, filename)
    print "processing %s" % filename
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        tmp = []
        for line in lines:
            tmp.append(line[:-1])
        file_str = ''.join(tmp)

        for i in range(0, len(file_str) - OPSEQ_LEN):
            rec[file_str[i:i + OPSEQ_LEN]] += 1
sorted_rec = list(reversed(sorted(rec.items(), key=operator.itemgetter(1))))

with open("feature_dict.txt", "w") as fw:
    features = [x[0] for x in sorted_rec[:100]]
    json.dump(features, fw)

print "Done"
