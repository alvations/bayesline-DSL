#!/bin/bash

for i in `seq 1 12`;
do
  for j in `seq 1 $i`;
  do
      python3 dsl-2019.py $j $i
  done
done
