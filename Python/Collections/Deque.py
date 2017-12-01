# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:07:43 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

from collections import deque

def switch1(value,x,d):
    result = {
      'append': lambda x: d.append(x),
      'appendleft': lambda x: d.appendleft(x),
      'pop': lambda x: d.pop(),
      'popleft': lambda x: d.popleft()
    }[value](x)

    return result

d=deque()

file1=open("Deque.txt","r")
N=int(file1.readline())

for i in range(N):
    st1=file1.readline().strip().split()
    if (len(st1)==1):
        switch1(st1[0],None,d)
    else:
        switch1(st1[0],int(st1[1]),d)
        
        
for element in d:
    print(element,end=" ")