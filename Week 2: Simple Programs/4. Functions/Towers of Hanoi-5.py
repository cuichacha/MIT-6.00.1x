#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:10:27 2019

@author: Will
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    elif a==0:
        return b
    elif a>b:
        return gcdRecur(b,a%b)
    else:
        return gcdRecur(a,b%a)