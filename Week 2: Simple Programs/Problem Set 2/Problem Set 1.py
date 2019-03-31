#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:28:45 2019

@author: Will
"""

annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def r_b(balance, month):
     if month==0:
          return balance
     else:
          return round(r_b(balance, month-1)*(1-monthlyPaymentRate)*(1+annualInterestRate/12), 2)
print("Remaining balance:", r_b(42, 12))