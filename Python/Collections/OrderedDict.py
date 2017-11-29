# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:44:34 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

from collections import OrderedDict


file=open('OrderedDict.txt','r')

ordered_dict = OrderedDict()
N=int(file.readline())

for i in range(N):
    st1=file.readline()
    item=""

    for i in st1.split()[:-1]:
        item=item+i+" "
    price=int(st1.split()[-1])
    item=item.strip(" ")

    if(item in ordered_dict):
        ordered_dict[item]=ordered_dict[item]+price   
    else:
        ordered_dict[item]=price
        
for k, v in ordered_dict.items():
    print(k,v)

