#!/usr/bin/env python -*- coding: utf-8 -*-

"""
Really raw version of `bayseline`. Will update with a proper API soon.
Now it only works for the DSL shared task: 
http://corporavm.uni-koeln.de/vardial/sharedtask.html
"""

import codecs, re, time
from itertools import chain

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def words_and_char_bigrams(text): # Unigram + 5grams.
    words = re.findall(r'\w{1,}', text)
    for w in words:
        yield w
        for i in range(len(w) - 5):
            yield w[i:i+5]

for n in range(1,20):
    start = time.time()
    # Training NB.
    train = []
    ngram_vectorizer = CountVectorizer(analyzer='char',ngram_range=(n, n), min_df=1)
    #ngram_vectorizer = CountVectorizer(analyzer=words_and_char_bigrams)
    mnb = MultinomialNB()
    trainset = ngram_vectorizer.fit_transform(codecs.open(trainfile,'r','utf8'))
    
    tags = list(chain(*[[l]*18000 for l in languages]))
    mnb.fit(trainset, tags)

    test = codecs.open(testfile,'r','utf8').readlines()
    testset = ngram_vectorizer.transform(test)
    results = mnb.predict(testset)
    testtags = [i.strip() for i in codecs.open(ansfile, 'r','utf8').readlines()]
    truepos = [x==y for x,y in zip(results,testtags)].count(True)
    #with codecs.open('5grams-char.out','w','utf8') as fout:
    #  for x,y in zip(results,testtags):
    #    print>>fout, x+"\t"+y 
    print n, len(ngram_vectorizer.get_feature_names()), trainset.getnnz()
    print truepos, truepos / float(len(testtags))
    print time.time() - start, 'secs'
    print

trainfile = 'train-a2e.txt'
testfile = 'test.txt'
ansfile = 'ans.txt'
# List of languages as ordered in train.txt.
languages = ['bs','hr','sr','id','my','cz','sk',
             'pt-BR','pt-PT','es-AR','es-ES']


'''
def train_classifier(trainfile, classifiers):
    """
    *trainfile* : Opened file.
    *classifier* : a classifer object.
    """    
    mnb = MultinomialNB()
    trainset = ngram_vectorizer.fit_transform(trainfile)
    ngram_vectorizer = CountVectorizer(analyzer='char',
                                       ngram_range=(n, n), min_df=1)
    trainset = ngram_vectorizer.fit_transform(trainfile)
'''

 
"""
 1 207 6549197
7395 0.672272727273
23.7153470516 secs

2 6364 28139482
8947 0.813363636364
30.2360780239 secs

3 69950 44407769
9917 0.901545454545
34.3617780209 secs

4 423875 50203717
10261 0.932818181818
42.9055738449 secs

5 1629139 52345885
10371 0.942818181818
61.7408359051 secs

6 4429090 53241254
10375 0.943181818182
93.7393698692 secs

7 8968190 53641518
10358 0.941636363636
149.373589993 secs

8 14446988 53824773
10300 0.936363636364
243.866472006 secs
"""