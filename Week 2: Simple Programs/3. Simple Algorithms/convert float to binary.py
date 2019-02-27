#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:49:54 2019

@author: Will
"""

num=float(input("Give a decimal number between 0 and 1: "))
p=0
while ((2**p)*num)%2!=0:
     p+=1
number=int((2**p)*num)
result=""
while number>0:
     result=str(number%2)+result
     number=number//2
final_result=int(result)/(10**p)
print(final_result)