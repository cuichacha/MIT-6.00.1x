#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 20:02:13 2019

@author: Will
"""

square=float(input("Give a number"))
epsilon=0.0001
guess=0.0
increment=0.0001
num_guesses=0
while abs(guess**2-abs(square))>=epsilon and abs(guess)<=abs(square):
     guess+=increment
     num_guesses+=1
     if abs(guess**2)>abs(square):
          guess-=increment
          increment/=10
print(guess)
print(num_guesses)