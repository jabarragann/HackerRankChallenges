# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:40:13 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

from itertools import product

file=open("04_MaximazeIt3.txt","r")

argArray= file.readline().split(" ")

numberOfLines=int(argArray[0])
modNumber=int(argArray[1])

arrays=[]
for i in range(numberOfLines):
    argArray=file.readline().split(" ")
    temp=[]
    for i in argArray:
        temp.append(int(i))        
    
    arrays.append(temp)


product1=list(product(*arrays))

maxNumb=0
for arg in product1:
    sum1=0
    for item in arg:
        sum1=sum1+item**2
        result=sum1%modNumber
    if result > maxNumb:
        maxNumb=result
        
print("Answer is: "+ str(maxNumb))

file.close()
