#!/usr/bin/env python -*- coding: utf-8 -*-

import codecs, string
from collections import defaultdict, Counter
from itertools import chain
from difflib import get_close_matches as gcm

from nltk import word_tokenize

def levenshtein(seq1, seq2):
    oneago = None
    thisrow = range(1, len(seq2) + 1) + [0]
    for x in xrange(len(seq1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
    return thisrow[len(seq2) - 1]

malay = [] 
indo = []
for i in codecs.open('train.txt','r','utf8'):
    if i.strip()[-2:] not in ['id','my']:
        continue
    sent, _, lang = i.strip().split('\t')
    if lang == "my":
        malay.append(sent)
    elif lang == "id":
        indo.append(sent)

malay_vocab = Counter(chain(*[word_tokenize(i) for i in malay]))
for i in list(malay_vocab):
    if malay_vocab[i] < 5:
        del malay_vocab[i]

indo_vocab = Counter(chain(*[word_tokenize(i) for i in indo]))
for i in list(indo_vocab):
    if indo_vocab[i] < 5:
        del indo_vocab[i]

for i in indo_vocab:
    if not i.isalpha or [j for j in i if j in string.punctuation]:
        continue
    try:
        int(i)
        continue
    except:
        pass
    
    matches = gcm(i, malay_vocab)
    if not matches:
        continue
    
    if i == matches[0]:
        #print i, matches[0]
        pass
    else:
        if levenshtein(i.lower(),matches[0].lower()) == 1 and \
        len(i) == len(matches[0]):
            print i, matches[0]