#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:28:52 2019

@author: Will
"""

square=float(input("Give a number"))
num_guesses=0
low=0
high=square
ans=(low+high)/2
epsilon=0.01
while abs(ans**2-square)>=epsilon:
     num_guesses+=1
     if ans**2<square:
          low=ans
     else:
          high=ans
     ans=(low+high)/2
print(num_guesses)
print(ans)