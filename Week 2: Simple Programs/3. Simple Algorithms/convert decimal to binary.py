#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:02:50 2019

@author: Will
"""

num=int(input("Give a number: "))
if num==0:
     print(num)
elif num<0:
     num=abs(num)
     Neg=True
else:
     Neg=False
result=""
while num>0:
     result=str(num%2)+result
     num=num//2
if Neg:
     print("-"+result)
else:
     print(result)