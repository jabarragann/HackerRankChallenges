# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:38:05 2017

@author: Juan Antonio Barragán
@email: jabarragann@unal.edu.co

Challenge taken from https://www.hackerrank.com/challenges/iterables-and-iterators/problem
check PNG images "03_.." for sreenshots of the instructions
"""

from itertools import combinations

n=4 
list1="a a c d".split(" ")
k=2

aIndexs=[i for i in range(len(list1)) if list1[i]=='a']

    
possibleIndex=[x for x in range(n)]
combinations=list(combinations(possibleIndex,k))
totalCombinations=len(combinations)

count=0

for i in combinations:
    if any([x==y for x in i for y in aIndexs]):
        count+=1
        
ans=count/totalCombinations
print(ans)