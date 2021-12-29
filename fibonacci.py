# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:01:21 2021

@author: javap
"""

def fibonacci(n):
    a,b=0,1
    print(a)
    print(b)
    print(a+b)
    for i in range(n-3):
        a,b=b,a+b
        print(a+b)