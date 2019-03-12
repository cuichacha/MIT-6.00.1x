#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:55:44 2019

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
    while exp>=1:
         result=result*base
         exp-=1
    return result