#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:53:56 2019

@author: Will
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result=1
    if exp==0:
        return result
    else: 
        return base*recurPower(base, exp-1)