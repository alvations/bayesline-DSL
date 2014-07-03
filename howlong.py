#!/usr/bin/env python -*- coding: utf-8 -*-

import os

def getsents(infile, ids):
    return [j.strip() for i,j in enumerate(open(infile, 'r')) if i in ids]
        

def gettags(infile):
    return [i.strip().split('\t')[-1] for i in open(infile)] 

def getnumtokens(infile):
    return [i.strip().split('\t')[0].count(" ") for i in open(infile)] 

def getnumchars(infile):
    return [len(i.strip().split('\t')[0]) for i in open(infile)]

"""
best_systems = {"nrc-catego-close-run3.txt",
                "rae-dslrae-closed-run1.txt",
                "michigan-umich-closed-run3.txt",
                "unimelbnlp-langidpy_pergrp_ngram-close-run2.txt",
                "qmul-systemd-close-run2.txt"}

sysoutdir = 'bestsysout'
goldfile = 'dslcc/test-gold.txt'
answers = gettags(goldfile)
tokenlens = getnumtokens(goldfile)
charlens = getnumchars(goldfile)
maxnumchar = len(max(open(goldfile, 'r'), key=len).strip())
ranges = zip(range(20,201,20), range(20,201,20)[1:])
ranges.append((200, maxnumchar))
    
for infile in os.listdir(sysoutdir):
    sysoutfile = "/".join([sysoutdir,infile])
    if sysoutfile == goldfile:
        continue
    ##print sysoutfile    
    for minimum, maximum in ranges:
        idx_in_range = [i for i,j in enumerate(tokenlens) if j > minimum and j < maximum+1]
        true_pos_idx = [i for i,j in enumerate(zip(gettags(sysoutfile), \
                                                      answers)) if j[0] == j[1] \
                                                      and i in idx_in_range]
        acc = len(true_pos_idx)/float(len(idx_in_range))
        '''
        false_pos_idx = [i for i,j in enumerate(zip(gettags(sysoutfile), \
                                                  answers)) if j[0] != j[1] \
                                                  and i in idx_in_range]
        print [answers[i] for i in false_pos_idx]
        for i in getsents(goldfile, false_pos_idx):
            print i
        '''
        print "\t".join(map(str,[str(minimum)+"-"+str(maximum), infile.partition('-')[0], \
        len(true_pos_idx), len(idx_in_range), "{0:.4f}".format(acc)]))
"""

#########################################################################

trainfile = "dslcc/train-a2e.txt"
maxnumchar = len(max(open(trainfile, 'r'), key=len).strip())
ranges = zip(range(20,201,20), range(20,201,20)[1:])
ranges.append((200, maxnumchar))
for minimum, maximum in ranges:
    idx_in_range = [i for i,j in enumerate(getnumtokens(trainfile)) if j > minimum and j < maximum+1]
    