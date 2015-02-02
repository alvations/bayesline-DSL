bayesline
=========

A Multinomial Bayesian Classification for Language Identification.

`bayseline.py` is used as a baseline system for the Discrimination of Similar Languages (DSL) shared task in COLING-2014 ((http://corporavm.uni-koeln.de/vardial/sharedtask.html). The best configuration of the system uses character 5grams as features and reports an overall accuracy of 94.3% . Detailed description of the DSLCC corpus and the performance of bayesline can be found: http://www.uni-koeln.de/~mzampier/papers/bucc2014.pdf

Cite
====

```
@article{tan2014merging,
  title={Merging Comparable Data Sources for the Discrimination of Similar Languages: The DSL Corpus Collection},
  author={Tan, Liling and Zampieri, Marcos and Ljube{\v{s}}ic, Nikola and Tiedemann, J{\"o}rg},
  journal={Proceedings of the 7th Workshop on Building and Using Comparable Corpora},
  pages={11--15},
  year={2014}
}
```

Dataset
====

The Disambiguating Similar Language Corpora Collection (DSLCC) files are formatted as tab-separated files, as such:

```
sent<tab>lang/variety group<tab>lang code
```

 - **DSLCC Training + Development Set**: https://db.tt/pRxy0IWW 
 - **DSLCC Test**: https://db.tt/av31jYYn
 - **DSLCC Gold**: https://db.tt/iLA6iY2D

**Note**: 

 - **DSLCC Train** contains 18,000 sentences per languagae/variety (lang/var), **DSLCC Devel** contains 2,000 sentences per lang/var
 - **DSLCC Test** contains 1,000 sentences per lang/var
 - **DSLCC Test** sentences are the same as the **DSLCC Gold**. It's just that **DSLCC Gold** contains the language code.
 - The `bayseline.py` only uses 18,000 from training dataset ;)
 - The official repo for the shared task is here: https://bitbucket.org/alvations/dslsharedtask2014

System Reults
====

![system reults](http://oi61.tinypic.com/2e56ttf.jpg)


Shared Task Results
====

![shared task](http://oi59.tinypic.com/a9phkw.jpg)
