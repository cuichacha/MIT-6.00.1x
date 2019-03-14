#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:43:42 2019

@author: Will
"""

# 一共有A，B，C三个柱子。一开始所有的盘子在柱子A，目标是将所有盘子移到柱子C
n=int(input("盘子的数量为 "))
def move(n, A, C, B):
     if n==1:
          print ("move from", A, "to", C)
     else:
          move(n-1, A, B, C)
          move(1, A, C, B)
          move(n-1, B, C, A)
print(move(n, "A", "C", "B"))