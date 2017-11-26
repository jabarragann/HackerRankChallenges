# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:43:50 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

from fractions import Fraction
from functools import reduce

def product(fracs):
    t =reduce(lambda x,y:x*y,fracs)
    return t.numerator, t.denominator


fracs=[Fraction(1,3),Fraction(1,7)]

result=product(fracs)

print(*result)

