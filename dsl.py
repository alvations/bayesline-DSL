# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

dsl2017 = {'train': 'DSLCC-2017/Train/DSL/DSL-TRAIN.txt',
           'dev': 'DSLCC-2017/Train/DSL/DSL-DEV.txt',
           'test': 'DSLCC-2015/Test/DSL/DSL-test.txt'}


def data(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        sentences, labels = zip(*[line.strip().split('\t') for line in fin])
        return sentences, labels

X_train, y_train = data(dsl2017['train'])
X_dev, y_dev = data(dsl2017['dev'])
#X_test, y_test = data(dsl['test'])

ngram_vectorizer = CountVectorizer(analyzer='char',
                                   ngram_range=(1, 5), min_df=1)

trainset = ngram_vectorizer.fit_transform(X_train)
tags = y_train
classifier = MultinomialNB()
classifier.fit(X_train, y_train)


predictions = classifier.predict(X_dev)
print (accuracy_score(y_dev, predictions))
