# -*- coding: utf-8 -*-

import os
import cPickle as pickle
from corpus import DSLCC, sents

dslcc = DSLCC()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train(train_docs, train_labels, n=5):
    ngram_vectorizer = CountVectorizer(analyzer='char',
                                       ngram_range=(n, n), min_df=1)
    trainset = ngram_vectorizer.fit_transform(train_docs)
    tags = train_labels
    classifier = MultinomialNB()
    classifier.fit(trainset, tags)
    return ngram_vectorizer, classifier 
    
def test(test_docs, goldtags, vectorizer, classifier, toevaluate=True):
    # Test
    testset = vectorizer.transform(test_docs)
    results = classifier.predict(testset)
    
    if not toevaluate:
        return results
    else:
        # Evaluate
        truepos = [x==y for x,y in zip(results,goldtags)].count(True)
        
        print len(vectorizer.get_feature_names()), 'features'
        print truepos, 'correct tags'
        print 'Accuracy:', truepos / float(len(goldtags))

def train_bayesline():
    """
    Trains the 5 character ngram classifier reported in BUCC 2014 and 
    DSL shared task 2014.
    """
    n = 5
    train_docs = dslcc.train_docs()
    train_labels = list(dslcc.train_labels())
    
    ngram_vectorizer, classifier  = train(train_docs, train_labels)    
    with open("bayseline.clf", "w") as fout:
        pickle.dump(classifier, fout)
        
    with open("bayseline.vectorizer", "w") as fout:
        pickle.dump(ngram_vectorizer, fout)
    return ngram_vectorizer, classifier

def load_bayesline():
    """
    Loads the default 5 character ngram classifier reported in BUCC 2014 and 
    DSL shared task 2014.
    """
    with open("bayseline.vectorizer", "rb") as fin1, \
    open("bayseline.clf", "rb") as fin2:
        return pickle.load(fin1), pickle.load(fin2)

def demo(tosave=True, toevaluate=True):
    if os.path.exists('bayseline.clf'):
        ngram_vectorizer, classifier = load_bayesline()
    else:
        ngram_vectorizer, classifier = train_bayesline()    
    if toevaluate:
        test_docs = dslcc.test_docs()
        goldtags = list(dslcc.gold_labels())
        test(test_docs, goldtags, ngram_vectorizer, classifier, toevaluate)
