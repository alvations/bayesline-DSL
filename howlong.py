import os

def gettags(infile):
    return [i.strip().split('\t')[-1] for i in open(infile)] 

def getnumtokens(infile):
    return [i.strip().split('\t')[0].count(" ") for i in open(infile)] 

def getnumchars(infile):
    return [len(i.strip().split('\t')[0]) for i in open(infile)]

best_systems = {"nrc-catego-close-run3.txt",
                "rae-dslrae-closed-run1.txt",
                "michigan-umich-closed-run3.txt",
                "unimelbnlp-langidpy_pergrp_ngram-close-run2.txt",
                "qmul-systemd-close-run2.txt"}

sysoutdir = 'sysout'
goldfile = 'sysout/test-gold.txt'
answers = gettags(goldfile)
tokenlens = getnumtokens(goldfile)
charlens = getnumchars(goldfile)

##print charlens
##print tokenlens

for i in os.listdir(sysoutdir):
    sysoutfile = "/".join([sysoutdir,i])
    if sysoutfile == goldfile:
        continue
    ##print sysoutfile
    
    true_pos_idx = [i for i,j in enumerate(zip(gettags(sysoutfile), \
                                                  answers)) if j[0] == j[1]]
    
    # True Positives.
    ##print [True for i,j in zip(gettags(sysoutfile), answers) if i == j]
    
    
    