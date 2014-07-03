#!/usr/bin/env python -*- coding: utf-8 -*-


import codecs, re, time
from itertools import chain

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def words_and_char_bigrams(text): # Unigram + 5grams.
    words = re.findall(r'\w{1,}', text)
    for w in words:
        yield w
        for i in range(len(w) - 5):
            yield w[i:i+5]


def train_classifier(trainfile, classifiers):
    """
    *trainfile* : Opened file.
    *classifier* : a classifer object.
    """    
    mnb = MultinomialNB()
    trainset = ngram_vectorizer.fit_transform(trainfile)
    ngram_vectorizer = CountVectorizer(analyzer='char',
                                       ngram_range=(n, n), min_df=1)