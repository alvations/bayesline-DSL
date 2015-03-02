# -*- coding: utf-8 -*-

import os

import corpus
import discriminate

# Runs this to create/load the bayesline.clf and bayesline.vectorizer
bayesline_vectorizer, bayesline_classifier =  discriminate.demo(toevaluate=False)

def tag(text,
        vectorizer= bayesline_vectorizer, 
        classifier= bayesline_classifier):
    return discriminate.tag(vectorizer, classifier, text)

