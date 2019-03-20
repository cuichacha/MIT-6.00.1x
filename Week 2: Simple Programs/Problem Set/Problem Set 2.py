#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:46:08 2019

@author: Will
"""

annualInterestRate = 0.2
lp=0
b=float(input("Balance: "))
bb=b
while bb>0:
     bb=b
     lp+=10
     for i in range(0,12):
          bb=(bb-lp)*(1+annualInterestRate/12)
print(lp)
