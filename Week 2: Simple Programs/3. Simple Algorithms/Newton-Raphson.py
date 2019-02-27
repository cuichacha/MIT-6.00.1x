#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:33:43 2019

@author: Will
"""
# x**2+x-6=(x+2)*(x-3)
# 无法解决多个根问题
epsilon=0.0001
guess=
num_guess=0
while abs(guess**2+guess-6)>=epsilon:
     num_guess+=1
     guess=guess-(guess**2+guess-6)/(guess*2+1)
print(num_guess)
print(guess)
     