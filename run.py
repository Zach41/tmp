#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess


def main():
    if len(sys.argv) != 3:
        print "usage: %s Opcode_length Algrithm" % sys.argv[0]
        sys.exit(1)
    alg = sys.argv[2]
    if not (alg == "DT" or alg == "KNN" or alg == "SVM"):
        print "Only support for 'DT' (for decision tree), 'KNN' and 'SVM' for now"
        sys.exit(1)
    os.environ["OPSEQ_LEN"] = sys.argv[1]
    os.environ["DETECT_ALG"] = alg

    subprocess.call(["python", "get_feature_dict.py"])
    subprocess.call(["python", "get_vec.py"])
    subprocess.call(["python", "classify.py"])


if __name__ == '__main__':
    main()
