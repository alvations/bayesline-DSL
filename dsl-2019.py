# -*- coding: utf-8 -*-

import sys
import time
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

import pandas as pd

def process_file(filename, task_name, data_split):
    with open(filename) as fin:
        for line in fin:
            text, label = line.strip().split('\t')
            yield {'task_name':task_name, 'data_split':data_split, 'text':text, 'label':label}
            
datasets = [
 ('vardial-2019/TRAININGSET-DMT_SIMP-VARDIAL2019/train.txt', 'DMT_SIMP', 'train'),
 ('vardial-2019/TRAININGSET-DMT_SIMP-VARDIAL2019/dev.txt',  'DMT_SIMP', 'dev'),
 ('vardial-2019/TRAININGSET-DMT_TRAD-VARDIAL2019/train.txt', 'DMT_TRAD', 'train'),
 ('vardial-2019/TRAININGSET-DMT_TRAD-VARDIAL2019/dev.txt', 'DMT_TRAD', 'dev'),
 
 ('vardial-2019/TRAININGSET-GDI-VARDIAL2019/train.txt', 'GDI', 'train'),
 ('vardial-2019/TRAININGSET-GDI-VARDIAL2019/dev.txt', 'GDI', 'dev'),
 
 ('vardial-2019/TRAININGSET-CLI-VARDIAL2019/train.txt', 'CLI', 'train'),
 ('vardial-2019/TRAININGSET-CLI-VARDIAL2019/dev.txt', 'CLI', 'dev'),
]    
        
data = []

for dataset in datasets:
    data += list(process_file(*dataset))
    
df = pd.DataFrame(data)

X_train = df[df['data_split'] == 'train']['text']
y_train = df[df['data_split'] == 'train']['label']

X_dev = df[df['data_split'] == 'dev']['text']
y_dev = df[df['data_split'] == 'dev']['label']

n_min, n_max = int(sys.argv[1]), int(sys.argv[2])

print (f'Model {n_min} to {n_max} grams...', end='\n', flush=True)

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

print (end='\n', flush=True)
