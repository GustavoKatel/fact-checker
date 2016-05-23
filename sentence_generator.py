#!/usr/bin/python
import nltk
from nltk.corpus import mac_morpho
import pickle

class SentenceGenerator:

    def __init__(self, base):
        self.base = base
        self.tagger = pickle.load(open("etc/mac_morpho_aubt.pickle"))

        self._tag()

    def __iter__(self):
        return self

    def _tag(self):
        self.tokens = []

        self.tokens += nltk.word_tokenize(self.base)

        self.base_tags = self.tagger.tag(self.tokens)

        self._find_groups()

    def _find_groups(self):
        self.groups = []

    def next(self):
        return self.base_tags
