#!/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import mac_morpho
import pickle
import random

import synonyms

class SentenceGenerator:

    def __init__(self, base):
        self.base = base
        self.tagger = pickle.load(open("etc/mac_morpho_aubt.pickle"))

        self._tag()

    def __iter__(self):
        return self

    def _tag(self):
        self.tokens = []

        self.tokens += [ w.lower() for w in nltk.word_tokenize(self.base) ]

        self.base_tags = self.tagger.tag(self.tokens)

        self._find_groups()

    def _find_groups(self):
        pattern = """
            NP: {<ART|PREP(\|\+)?|DET|ADJ|KS|KC|N|PROPESS>*}
            V: {<V>}
        """
        chunker_fast = nltk.RegexpParser(pattern)

        chunk_result = chunker_fast.parse(self.base_tags)

        self.groups = [self._parse_tree(gp) for gp in chunk_result]

    def _parse_tree(self, tree):
        if type(tree) == nltk.Tree:
            return [self._parse_tree(gp) for gp in tree]

        return tree #.label()

    def _replace_synonym(self, tagged_sentence):

        sentence = []
        for (i,(word, tag)) in enumerate(tagged_sentence):
            if tag == 'N' and random.randint(0,1)==1:
                syns = synonyms.get_synonyms(word)[1:]

                new_word = random.sample(syns, 1)

                sentence.append(new_word[0])

            else:
                sentence.append(word)

        return sentence

    def next(self):

        rand_groups = random.sample(self.groups, len(self.groups))
        # rand_indexes = range(len(self.groups))
        # random.shuffle(rand_indexes)

        # rand_groups = []
        # for i in rand_indexes:
            # rand_groups.append(self.groups[i])

        rand_sentence = []

        # return self.groups
        # return rand_groups
        for gp in rand_groups:
            rand_sentence += [ (text, tag) for (text, tag) in gp ]

        return ' '.join(self._replace_synonym(rand_sentence))
        # return rand_sentence
        # return ' '.join(rand_sentence)
