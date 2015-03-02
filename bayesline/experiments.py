# -*- coding: utf-8 -*-

import re

import discriminate
from corpus import DSLCC

dslcc = DSLCC()

def blind_CAPS(text):
    return re.sub('(?:[A-Z][\w]+\s*)', ' #NE# ', text)

def blind_CAPS_without_first_word(text):
    first_word, _, the_rest = text.partition(' ')
    blinded = re.sub('(?:[A-Z][\w]+\s*)', ' #NE# ', the_rest)
    return " ".join([first_word, blinded])

def blind_ne_experiment(blind_function):
    # Blind.
    blind = blind_function
    train_docs = [blind(doc) for doc in dslcc.train_docs()]
    test_docs = [blind(doc) for doc in dslcc.test_docs()]
    
    # Train.
    train_labels = list(dslcc.train_labels())
    vectorizer, classifier = discriminate.train(train_docs, train_labels)
    
    # Test.
    goldtags = list(dslcc.gold_labels())
    discriminate.test(test_docs, goldtags, vectorizer, classifier)


blind_ne_experiment(blind_CAPS)
print 
blind_ne_experiment(blind_CAPS_without_first_word)

