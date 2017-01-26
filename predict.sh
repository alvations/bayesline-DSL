#!/bin/bash

for i in `seq 1 6`;
do
  for j in `seq $i 6`;
  do
    python3 predict.py bayesline.$1_to_$j-gram.vectorizer bayesline.$i_to_$j-gram.classifier > outputs/$1_to_$j.out
  done
done
