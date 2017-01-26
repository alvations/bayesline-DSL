# -*- coding: utf-8 -*-

import time
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

dsl2017 = {'train': 'DSLCC-2017/Train/DSL/DSL-TRAIN.txt',
           'dev': 'DSLCC-2017/Train/DSL/DSL-DEV.txt',
           'test': 'DSLCC-2015/Test/DSL/DSL-test.txt'}


def data(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        sentences, labels = [], []
        for line in fin:
            x, y = line.strip().split('\t')
            sentences.append(x)
            labels.append(y)
        return sentences, labels

X_train, y_train = data(dsl2017['train'])
X_dev, y_dev = data(dsl2017['dev'])
#X_test, y_test = data(dsl['test'])

print ('Vectorizing...', end='')
start = time.time()
ngram_vectorizer = CountVectorizer(analyzer='char',
                                   ngram_range=(1, 5), min_df=1)
trainset = ngram_vectorizer.fit_transform(X_train)
tags = y_train
end = time.time() - start
print ('took {} seconds.'.format(end))

with open('bayesline.vectorizer', 'wb') as fout:
    pickle.dump(ngram_vectorizer, fout)

print ('Training... ', end='')
start = time.time()
classifier = MultinomialNB()
classifier.fit(X_train, y_train)
end = time.time() - start
print ('took {} seconds.'.format(end))

with open('bayesline.classifier', 'wb') as fout:
    pickle.dump(classifier, fout)

predictions = classifier.predict(X_dev)
print (accuracy_score(y_dev, predictions))
