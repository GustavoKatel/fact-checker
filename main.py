#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import itertools

from sentence_generator import SentenceGenerator

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File name with the text to tag")

    args = parser.parse_args()

    f = open(args.filename, "rU")
    lines = f.readlines()
    f.close()

    generators = []

    for line in lines:
        generators.append(SentenceGenerator(line.decode("utf-8")))

    for generator in generators:
        for i in range(5):
            print generator.next()
