Bayesline
====

This is similar to Tan et al. (2014) system in DSL-2014 task. It's a multinomial
naive bayes classifier on the dataset. No special parameter tuning was done.

- Run1: Only character 4-grams features
- Run2: Only character 5-grams features
- Run3: Character 1 to 5-grams features

The feature sets for the runs above are selected by an exhaustive search
strategy use in Scarton et al. (2015).


Reference
====

- Liling Tan, Marcos Zampieri, Nikola Ljubešic, and Jörg Tiedemann. 2014. Merging comparable data sources for the discrimination of similar languages: The DSL corpus collection. In Proceedings of the 7th Workshop on Building and Using Comparable Corpora (BUCC).

- Carolina Scarton, Liling Tan, Lucia Specia. 2015. USHEF and USAAR-USHEF Participation in the WMT15 Quality Estimation Shared Task. In Proceedings of Proceedings of the 10th Workshop on Statistical Machine Translation (WMT).
