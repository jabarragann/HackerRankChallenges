# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:47:43 2017

@author: Santi
"""

#lambda function examples 

print("")
print("1.Sum Function")

sum = lambda a,b,c: a+b+c

print(sum(1,2,3))

#example 2

'''
When using the sorting function a key parameter
my be added to specify the which value should be
use for sorting purposes.

The key must be a function that takes a single
argument and returns a key to use for sorting
purposes.

https://wiki.python.org/moin/HowTo/Sorting
'''

print("\n2.Sorting by especific value")
student_tuples = [
        ('david', 'A', 15),
        ('jane', 'B', 12),
        ('alex', 'E', 10),
]

sorted_students=sorted(student_tuples, key=lambda student: student[1])

for i in sorted_students:
    print(i)

#example 3 

print("\n3.Get a list of the cube of the fibonnacci numbers. MAP and LAMBDA example")

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    init1=0
    init2=1
    fibolist=[init1,init2]
    for i in range(n-2):
        fibolist.append(fibolist[-1]+fibolist[-2])
    
    if(n==1):
        return [0]
    elif (n==0):
        return []
    else:
        return fibolist
         
if __name__=='__main__':    
    print(list(map(cube,fibonacci(10))))
        
        
