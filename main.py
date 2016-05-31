#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import itertools
import webbrowser

from sentence_generator import SentenceGenerator

import synonyms

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
        print 'Base: ' + generator.base
        for i in range(5):
            sentence = generator.next()
            print sentence
            webbrowser.open('https://www.google.com.br/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q='+sentence.replace(' ', '+'))
        print '-------------------'
        print
