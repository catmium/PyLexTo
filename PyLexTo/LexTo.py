#!/usr/bin/python
# -*- coding: utf-8 -*-

import jpype
from os import path, walk


class LexTo(object):
    def __init__(self, word_list=None):
        dir_path = path.abspath(path.dirname(__file__))
        jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', '-Djava.class.path={0}/LongLexTo'.format(dir_path))
        LongLexTo = jpype.JClass('LongLexTo')
        self.tokenizer = LongLexTo(dir_path + '/data/dictionary', word_list)
        self.stopwords = []
        for root, dirs, files in walk(dir_path + '/data/stopwords'):
            for file in files:
                if file.endswith('stopwords.txt'):
                    with open(path.join(root, file)) as f:
                        for w in f.readlines():
                            self.stopwords.append(w.strip())
        self.type_string = {0: "unknown",
                            1: "known",
                            2: "ambiguous",
                            3: "English/Digits",
                            4: "special"}

    def tokenize(self, line, remove_stopwords=False, remove_space=False):
        line = line.strip()
        line = line.replace(u'ํา', u'ำ')
        self.tokenizer.wordInstance(line)
        type_list = self.tokenizer.getTypeList()
        type_list = [self.type_string[n.value] for n in type_list]
        word_list = []
        begin = self.tokenizer.first()
        while self.tokenizer.hasNext():
            end = self.tokenizer.next()
            word_list.append(line[begin:end])
            begin = end
        idx2brm = []
        if remove_stopwords:
            for i, w in enumerate(word_list):
                if w in self.stopwords:
                    idx2brm.append(i)
            word_list = [w for i, w in enumerate(word_list) if i not in idx2brm]
            type_list = [w for i, w in enumerate(type_list) if i not in idx2brm]
        idx2brm = []
        if remove_space:
            for i, w in enumerate(word_list):
                if len(w.strip()) == 0:
                    idx2brm.append(i)
            word_list = [w for i, w in enumerate(word_list) if i not in idx2brm]
            type_list = [w for i, w in enumerate(type_list) if i not in idx2brm]
        return word_list, type_list
