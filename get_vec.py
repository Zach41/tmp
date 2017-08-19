#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import path
import json

malware_vecs = []
benign_vecs = []
features = []

OPSEQ_LEN = int(os.environ.get("OPSEQ_LEN", 12))

print "Generating Vectors with OPSEQ Length %d" % OPSEQ_LEN

with open("feature_dict.txt", 'r') as fr:
    features = json.load(fr)

m_idx = {}
for i in range(len(features)):
    m_idx[features[i]] = i

print "Malwares traning dataset"

MTRAININGSET_PATH = path.join("malwares_opseq", "training_set")
BTRAININGSET_PATH = path.join("benign_opseq", "training_set")

for filename in os.listdir(MTRAININGSET_PATH):
    if not filename.endswith("opseq"):
        continue
    print "\tprocessing %s" % filename
    feature = [0] * len(features)
    tmp = []
    with open(os.path.join(MTRAININGSET_PATH, filename), 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            tmp.append(line[:-1])
    file_str = ''.join(tmp)

    for i in range(0, len(file_str) - OPSEQ_LEN):
        if file_str[i:i+OPSEQ_LEN] in m_idx:
            feature[m_idx[file_str[i:i+OPSEQ_LEN]]] = 1
    malware_vecs.append(feature)

print "Benigns training dataset"

for filename in os.listdir(BTRAININGSET_PATH):
    if not filename.endswith("opseq"):
        continue
    print "\tprocessing %s" % filename
    feature = [0] * len(features)
    tmp = []
    with open(os.path.join(BTRAININGSET_PATH, filename), 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            tmp.append(line[:-1])
    file_str = ''.join(tmp)

    for i in range(0, len(file_str) - OPSEQ_LEN):
        if file_str[i:i+OPSEQ_LEN] in m_idx:
            feature[m_idx[file_str[i:i+OPSEQ_LEN]]] = 1
    benign_vecs.append(feature)

with open("malware_vecs.txt", "w") as fw:
    json.dump(malware_vecs, fw)

with open("benign_vecs.txt", "w") as fw:
    json.dump(benign_vecs, fw)

print "Done"
