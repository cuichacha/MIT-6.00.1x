#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:19:04 2019

@author: Will
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a==b:
        return a
    elif a>b:
        i=b
        while a%i!=0 or b%i!=0 and i>1:
            i=i-1
        return i
    else:
        i=a
        while a%i!=0 or b%i!=0 and i>1:
            i=i-1
        return i