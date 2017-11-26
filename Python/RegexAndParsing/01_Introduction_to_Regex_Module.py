# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:32:36 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
   
   

#check floating numbers

def checkForFloats(num):
    reg="^(([+|-])?[0-9]*\.[0-9]+)$"
    
    return bool(re.match(reg,num))


print(checkForFloats("-0.69"))