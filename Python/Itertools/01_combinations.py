# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:08:44 2017

@author: Santi
"""

from itertools import combinations


str1="santi"
print("Generate all combinations 2 letter combinations of "+ str1)    
comb=list(combinations(str1,2))
comb=sorted(comb)

for i in comb:
    print(i)