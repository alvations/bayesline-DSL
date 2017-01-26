# -*- coding: utf-8 -*-

import sys
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
            x, *y = line.strip().split('\t')
            sentences.append(x)
            if y:
                labels.append(y[0])
        return sentences, labels

X_train, y_train = data(dsl2017['train'])
X_dev, y_dev = data(dsl2017['dev'])
#X_test, y_test = data(dsl['test'])


n_min, n_max = int(sys.argv[1]), int(sys.argv[2])

print ('Vectorizing...', end='', flush=True)
start = time.time()
ngram_vectorizer = CountVectorizer(analyzer='char',
                                   ngram_range=(n_min, n_max), min_df=1)
trainset = ngram_vectorizer.fit_transform(X_train)
tags = y_train
end = time.time() - start
print ('took {} seconds.'.format(end), flush=True)

with open('bayesline.{}_to_{}-gram.vectorizer'.format(n_min, n_max), 'wb') as fout:
    pickle.dump(ngram_vectorizer, fout)

print ('Training... ', end='', flush=True)
start = time.time()
classifier = MultinomialNB()
classifier.fit(trainset, tags)
end = time.time() - start
print ('took {} seconds.'.format(end), flush=True)

with open('bayesline.{}_to_{}-gram.classifier'.format(n_min, n_max), 'wb') as fout:
    pickle.dump(classifier, fout)

devset = ngram_vectorizer.transform(X_dev)
predictions = classifier.predict(devset)
print (accuracy_score(y_dev, predictions))
