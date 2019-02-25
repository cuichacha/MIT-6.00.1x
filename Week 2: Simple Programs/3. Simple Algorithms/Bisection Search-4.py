#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:36:25 2019

@author: Will
"""

cube=float(input("Give a number"))
num_guesses=0
epsilon=0.01
if cube>0:
     low=0
     high=cube
     ans=(low+high)/2
     while abs(ans**3-cube)>=epsilon:
          if (ans**3)>cube:
               high=ans
          else:
               low=ans
          num_guesses+=1
          ans=(low+high)/2
else:
     high=0
     low=cube
     ans=(low+high)/2
     while abs(ans**3-cube)>=epsilon:
          if abs(ans**3)>abs(cube):
               low=ans
          else:
               high=ans
          num_guesses+=1
          ans=(low+high)/2
print(num_guesses)
print(ans)