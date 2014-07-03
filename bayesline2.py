#!/usr/bin/env python -*- coding: utf-8 -*-

import codecs
import cPickle as pickle

def default_vectorizer():
    
    return vectorizer
    
def train_classifier(docsfile, labelsfile, modelfile, vectorizerfile, 
                    classifier=None, vectorizer=None):
    """
    *docsfile*: document file for training.
    *labelsfile*: label file for training.
    *classifier*: a classifer object.
    *vectorizer*: feature analyzer.
    """    
    if not classifier: # Use Multinomial Naive Bayes if no classifier specified.
        from sklearn.naive_bayes import MultinomialNB
        classifer = MultinomialNB() 
    
    if not vectorizer: # Use default character 5grams vectorizer.
       from sklearn.feature_extraction.text import CountVectorizer
       vectorizer = CountVectorizer(analyzer='char', 
                                    ngram_range=(1, 5), min_df=1)
        
    # Load training documents and labels files.
    trainfile = codecs.open(docsfile,'r','utf8') 
    tags = [i.strip() for i in codecs.open(labelsfile, 'r', 'utf8')]
    # Vectorize training documents.
    trainset = vectorizer.fit_transform(trainfile)
    # Train classification model.
    classifer.fit(trainset, tags)
    # Dumps model into a pickle.
    with open(modelfile, 'wb') as fout1, open(vectorizerfile, 'wb') as fout2:
        pickle.dump(classifier, fout1)
        pickel.dump(vectorizer, fout2)
           
def load_pickle(pkfile):
    """ Loads a pickled file. """
    with open(pkfile, 'rb') as fin:
        return pickle.load(fin)

def tag(testfile, modelfile, vectorizerfile):    
    """
    Tags the data, given the test documents and the pickled model file.
    """
    # Load classifer and vectorizer.
    classifier = load_pickle(modelfile)
    vectorizer = load_pickle(vectorizerfile)
    # Loads test documents.
    test = codecs.open(testfile,'r','utf8').readlines()
    # Vectorize test documents.
    testset = vectorizer.transform(test)
    # Assigns labels to test documents.
    results = classifier.predict(testset)
    return results

#########################################################################

# Training 
traindocs = 'dslcc/train-docs.txt'
trainlabels = 'dslcc/train-labels.txt'

outmodelfile = 'dsl-5chargrams.model'
outvecfile = 'dsl-5chargrams.vectorizer'
train_classifier(traindocs, trainlabels, outmodelfile, outvecfile)

testfile = 'dslcc/test.txt'


    
    
'''
def train_classifier(trainfile, classifier=None, analyzer=None):
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNBs
    
    if not classifier: # Use Multinomial Naive Bayes if no classifier specified.
        classifer = MultinomialNB() 
    
    trainset = ngram_vectorizer.sfit_transform(trainfile)
    
'''