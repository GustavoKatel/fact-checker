#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import mac_morpho
import pickle
import argparse

tagger = pickle.load(open("etc/mac_morpho_aubt.pickle"))

def tag(filename):
    f = open(filename, "rU")
    lines = f.readlines()
    f.close()

    tokens = []

    for line in lines:
        tokens += nltk.word_tokenize(line.decode("utf-8"))

    print tagger.tag(tokens)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File name with the text to tag")

    args = parser.parse_args()

    tag(args.filename)
