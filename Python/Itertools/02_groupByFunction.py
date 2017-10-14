# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:15:47 2017

@author: Santi
"""

#group by function


from itertools import groupby 

keys=[k for k, g in groupby('AAAABBBCCDAABBB')] 
groups=[list(g) for k, g in groupby('AAAABBBCCD')]

print(keys)
print(groups)

test_str="1222311"

for k, g in groupby(test_str):
    print( "("+k+","+str(len(list(g)))+")" )
    
    
    
