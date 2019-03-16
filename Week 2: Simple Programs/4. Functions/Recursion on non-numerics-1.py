#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:54:15 2019

@author: Will
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr=="":
         return False
    if char==aStr[int(len(aStr)/2)]:
         return True
    elif char>aStr[int(len(aStr)/2)] and int(len(aStr)/2)!=0:
        return isIn(char, aStr[int(len(aStr)/2):])
    elif char<aStr[int(len(aStr)/2)] and int(len(aStr)/2)!=0:
        return isIn(char, aStr[0:int(len(aStr)/2)])
    else:
        return False
