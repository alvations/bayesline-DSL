# -*- coding: utf-8 -*-

import io

def sents(infile):
    """ Lazy corpus reader that yields line. """
    with io.open(infile, 'r', encoding='utf8') as fin:
        for line in fin:
            yield line.strip()

class DSLCC:
    """
    Corpus interface for Discriminating Similar Language 
    Corpus Collection (DSLCC), see http://goo.gl/BQBhkW
    
    >>> dslcc = DSLCC()
    >>> for i, j in dslcc.test():
    ...     print j, i
    
    """
    # Training data.
    def train_docs(self):
        return sents('dslcc/train-docs.txt')
    def train_labels(self):
        return sents('dslcc/train-labels.txt')
        
    def train(self):
        """ Yields document and labels concurrently """
        for doc, label in zip(self.train_docs(), self.train_labels()):
            yield doc, label
    
    # Test data.
    def test_docs(self):
        return sents('dslcc/test-docs.txt')
    def gold_labels(self):
        return sents('dslcc/gold-labels.txt')

    def test(self):
        """ Yields document and labels concurrently """
        for doc, label in zip(self.test_docs(), self.test_labels()):
            yield doc, label

    