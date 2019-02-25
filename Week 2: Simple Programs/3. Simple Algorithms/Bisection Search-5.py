#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:11:03 2019

@author: Will
"""

cube=float(input("Give a number"))
num_guesses=0
epsilon=0.00000000001
if cube>1:
     low=0
     high=cube
elif 0<cube<1:
     high=1
     low=cube
elif -1<cube<0:
     high=cube
     low=-1
else:
     high=0
     low=cube
ans=(low+high)/2
while abs(ans**3-cube)>=epsilon and cube>0:
     if (ans**3)>cube:
          high=ans
     else:
          low=ans
     num_guesses+=1
     ans=(low+high)/2
while abs(ans**3-cube)>=epsilon and cube<0:
     if abs(ans**3)>abs(cube):
          low=ans
     else:
          high=ans
     num_guesses+=1
     ans=(low+high)/2
print(num_guesses)
print(ans)