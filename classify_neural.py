#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from sklearn.neural_network import MLPClassifier
from collections import defaultdict

vocabularies = []
training_data = []
training_labels = []

with open("vocabularies.txt", 'r') as fr:
    vocabularies.extend(json.load(fr))

with open("neural_vec_malwares.txt", 'r') as fr:
    data = json.load(fr)
    training_data.extend(data)
    training_labels.extend([1] * len(data))

with open("neural_vec_benigns.txt", 'r') as fr:
    data = json.load(fr)
    training_data.extend(data)
    training_labels.extend([0] * len(data))

clf = MLPClassifier(
    solver='sgd', activation='logistic')
clf.fit(training_data, training_labels)

false_cnt = 0
true_cnt = 0
total_cnt = 0
for filename in os.listdir("test_opseq"):
    if not filename.endswith("opseq"):
        continue
    total_cnt += 1
    file_vec = [0] * len(vocabularies)
    word_cnt = defaultdict(int)
    total_word_cnt = 0
    file_str = []
    with open(os.path.join("test_opseq", filename), 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            file_str.append(line.strip())
    file_str = ''.join(file_str)
    for i in range(0, len(file_str) - 10, 10):
        word_cnt[file_str[i:i + 10]] += 1
    for i in range(len(vocabularies)):
        if vocabularies[i] in word_cnt:
            total_word_cnt += word_cnt[vocabularies[i]]
            # file_vec[i] = float(word_cnt[vocabularies[i]]) / float(
            #     total_word_cnt)
            file_vec[i] = 1
    if (clf.predict([file_vec])[0]):
        print "%s is malware" % filename
        if filename.startswith("malware"):
            true_cnt += 1
        else:
            false_cnt += 1
    else:
        print "%s is benign" % filename
        if filename.startswith("benign"):
            true_cnt += 1
        else:
            false_cnt += 1
print "\nTrue Rate: %s" % (float(true_cnt) / float(total_cnt))
print "\nFlase Rate: %s" % (float(false_cnt) / float(total_cnt))
