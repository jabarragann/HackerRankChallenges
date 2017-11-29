# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:41:28 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

from collections import namedtuple

inputFile=open('NamedTupledInput.txt','r')

N,headers=[inputFile.readline().strip('\n') for i in range(2)]

spreadSheet=[l1.strip('\n') for l1 in inputFile]

Student = namedtuple('Student', headers)
students= [Student(*std.split()) for std in spreadSheet]

ans=sum( map(lambda x: int(x.MARKS), students))/int(N)

print(ans)




