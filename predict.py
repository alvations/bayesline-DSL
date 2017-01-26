# -*- coding: utf-8 -*-

import sys
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

dsl2017 = {'train': 'DSLCC-2017/Train/DSL/DSL-TRAIN.txt',
           'dev': 'DSLCC-2017/Train/DSL/DSL-DEV.txt',
           'test': 'DSLCC-2017/Test/DSL/DSL-test.txt'}


def data(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        sentences, labels = [], []
        for line in fin:
            x, *y = line.strip().split('\t')
            sentences.append(x)
            if y:
                labels.append(y[0])
        return sentences, labels


vectorizer_filename = sys.argv[1]
classifer_filename = sys.argv[2]

with open(vectorizer_filename, 'rb') as fin:
    vectorizer = pickle.load(fin)

with open(classifer_filename, 'rb') as fin:
    classifier = pickle.load(fin)

X_test, _ = data(dsl2017['test'])

testset = vectorizer.transform(X_test)
predictions = classifier.predict(testset)

for p in predictions:
    print (p)
