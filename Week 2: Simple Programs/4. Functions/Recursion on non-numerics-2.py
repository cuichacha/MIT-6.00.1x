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
    if char==aStr[len(aStr)//2]:
         return True
    elif char>aStr[len(aStr)//2] and len(aStr)//2!=0:
        return isIn(char, aStr[len(aStr)//2:])
    elif char<aStr[len(aStr)//2] and len(aStr)//2!=0:
        return isIn(char, aStr[0:len(aStr)//2])
    else:
        return False
