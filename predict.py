# -*- coding: utf-8 -*-

import sys

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

from dsl import data, dsl2017

open(this_directory + "/bayesline.clf", "rb") as fin2:
    vectorizer, classifier =  pickle.load(fin1), pickle.load(fin2)

vectorizer_filename = sys.argv[1]
classifer_filename = sys.argv[2]

with (vectorizer_filename, 'rb') as fin:
    vectorizer = pickle.load(fin)

with (classifer_filename, 'rb') as fin:
    classifier = pickle.load(fin)

X_test, _ = data(dsl['test'])

testset = vectorizer.transform(X_test)
predictions = classifier.predict(devset)

for p in predictions:
    print (p)
