# -*- coding: utf-8 -*-

import os, sys, time
import cPickle as pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from corpus import DSLCC, sents

dslcc = DSLCC()
this_directory = os.path.dirname(os.path.realpath(__file__))

def train(train_docs, train_labels, 
          classifier_choice= MultinomialNB,
          n=5):
    ngram_vectorizer = CountVectorizer(analyzer='char',
                                       ngram_range=(n, n), min_df=1)
    trainset = ngram_vectorizer.fit_transform(train_docs)
    tags = train_labels
    classifier = classifier_choice()
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

def tag(vectorizer, classifier, texts):
    if isinstance(texts, (str, unicode)):
        # If input is a single sentence.
        return classifier.predict(vectorizer.transform([texts]))[0]
    else:
        return classifier.predict(vectorizer.transform(texts))

def train_bayesline():
    """
    Trains the 5 character ngram classifier reported in BUCC 2014 and 
    DSL shared task 2014.
    """
    n = 5
    train_docs = dslcc.train_docs()
    train_labels = list(dslcc.train_labels())
    
    ngram_vectorizer, classifier  = train(train_docs, train_labels)    
    with open(this_directory +  "/bayesline.clf", "w") as fout:
        pickle.dump(classifier, fout)
        
    with open(this_directory +  "/bayesline.vectorizer", "w") as fout:
        pickle.dump(ngram_vectorizer, fout)
    return ngram_vectorizer, classifier

def load_bayesline():
    """
    Loads the default 5 character ngram classifier reported in BUCC 2014 and 
    DSL shared task 2014.
    """
    sys.stderr.write('Loading Bayesline.py ... ')
    with open(this_directory +  "/bayesline.vectorizer", "rb") as fin1, \
    open(this_directory + "/bayesline.clf", "rb") as fin2:
        vectorizer, classifier =  pickle.load(fin1), pickle.load(fin2)
    sys.stderr.write('Loaded and ready to tag !!! \n')
    return vectorizer, classifier 
    

def demo(tosave=True, toevaluate=True):
    this_directory = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(this_directory + '/bayesline.clf'):
        ngram_vectorizer, classifier = load_bayesline()
    else:
        ngram_vectorizer, classifier = train_bayesline()    
    if toevaluate:
        test_docs = dslcc.test_docs()
        goldtags = list(dslcc.gold_labels())
        test(test_docs, goldtags, ngram_vectorizer, classifier, toevaluate)
    return ngram_vectorizer, classifier
