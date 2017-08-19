#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

OPSEQ_LEN = int(os.environ.get("OPSEQ_LEN", 10))
# DT (Decision Tree), KNN, SVM
DETECT_ALG = os.environ.get("DETECT_ALG", "DT")

training_data = []
labels = []
features = []

print "Using %s algorithm with opcode length %d" % (DETECT_ALG, OPSEQ_LEN)

with open("feature_dict.txt", 'r') as fr:
    features = json.load(fr)

m_idx = {}
for i in range(len(features)):
    m_idx[features[i]] = i

with open("malware_vecs.txt", "r") as fr:
    arr = json.load(fr)
    training_data.extend(arr)
    labels.extend([1] * len(arr))

with open("benign_vecs.txt", "r") as fr:
    arr = json.load(fr)
    training_data.extend(arr)
    labels.extend([0] * len(arr))

if DETECT_ALG == "SVM":
    clf = svm.SVC()
elif DETECT_ALG == "DT":
    clf = tree.DecisionTreeClassifier()
elif DETECT_ALG == "KNN":
    clf = KNeighborsClassifier()
else:
    clf = tree.DecisionTreeClassifier()

clf.fit(training_data, labels)

false_cnt = 0
total_cnt = 0
true_cnt = 0
for filename in os.listdir("test_opseq"):
    if not filename.endswith("opseq"):
        continue
    total_cnt += 1
    feature = [0] * len(features)
    tmp = []
    with open(os.path.join("test_opseq", filename), 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            tmp.append(line[:-1])
    file_str = ''.join(tmp)

    for i in range(0, len(file_str) - OPSEQ_LEN):
        if file_str[i:i + OPSEQ_LEN] in m_idx:
            feature[m_idx[file_str[i:i + OPSEQ_LEN]]] = 1

    if clf.predict([feature])[0]:
        if filename.startswith("malware"):
            true_cnt += 1
        else:
            false_cnt += 1
    else:
        if filename.startswith("benign"):
            true_cnt += 1
        else:
            false_cnt += 1
print "\n\nTrue Rate: %s" % (float(true_cnt) / float(total_cnt))
