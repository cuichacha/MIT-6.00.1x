#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:32:42 2019

@author: Will
"""

annualInterestRate = 0.2
lp=0
b=float(input("Balance: "))
bb=b
lower_bound=b/12
upper_bound=(b*(1+annualInterestRate/12)**12)/12
lp=(lower_bound+upper_bound)/2
while abs(bb)*1000>1:
     bb=b
     for i in range(0,12):
          bb=(bb-lp)*(1+annualInterestRate/12)
     if bb>0:
          lower_bound=lp
     else:
          upper_bound=lp
     lp=(lower_bound+upper_bound)/2
print(round(lp,2))