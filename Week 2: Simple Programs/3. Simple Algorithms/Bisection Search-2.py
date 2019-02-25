#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:47:12 2019

@author: Will
"""

cube=float(input("Give a number"))
test=True
epsilon=0.01
guess=(cube/2)
num_guesses=0
while test:
     num_guesses+=1
     if abs((guess**3))-abs(cube)>=epsilon:
          guess/=2
     else:
          guess=guess*3/2
     if(epsilon/10)<=abs((guess**3))-abs(cube)<epsilon:
          break
print(num_guesses)
print(guess)