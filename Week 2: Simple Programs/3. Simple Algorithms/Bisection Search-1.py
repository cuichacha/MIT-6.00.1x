#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:49:59 2019

@author: Will
"""

square=float(input("Give a number"))
test=True
epsilon=0.01
guess=(square/2)
num_guesses=0
while test:
     num_guesses+=1
     if (guess**2)-abs(square)>=epsilon:
          guess/=2
     else:
          guess=guess*3/2
     if(epsilon/10)<=(guess**2)-abs(square)<epsilon:
          break
print(num_guesses)
print(guess)
