#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:23:57 2019

@author: Will
"""

cube=float(input("Give a number"))
num_guesses=0
epsilon=0.0000001
low=cube
high=1
ans=(low+high)/2
while abs(ans**3-cube)>=epsilon:
     if abs(ans**3)>abs(cube):
          high=ans
     else:
          low=ans
     num_guesses+=1
     ans=(low+high)/2
print(num_guesses)
print(ans)