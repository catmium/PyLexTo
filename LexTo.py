#!/usr/bin/python
# -*- coding: utf-8 -*-

import jpype
from os import path


class LexTo(object):
    def __init__(self):
        file_path = path.abspath(path.dirname(__file__))
        jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', '-Djava.class.path={0}/LongLexTo'.format(file_path))
        LongLexTo = jpype.JClass('LongLexTo')
        self.tokenizer = LongLexTo('./data/dictionary')
        self.type_string = {0: "unknown",
                            1: "known",
                            2: "ambiguous",
                            3: "English/Digits",
                            4: "special"}

    def tokenize(self, line):
        line = line.strip()
        self.tokenizer.wordInstance(line)
        type_list = self.tokenizer.getTypeList()
        type_list = [self.type_string[n.value] for n in type_list]
        word_list = []
        begin = self.tokenizer.first()
        while self.tokenizer.hasNext():
            end = self.tokenizer.next()
            word_list.append(line[begin:end])
            begin = end
        return word_list, type_list
