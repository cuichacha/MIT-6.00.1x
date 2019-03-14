#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:53:03 2019

@author: Will
"""

# 一共有A，B，C三个柱子。一开始所有的盘子在柱子A，目标是将所有盘子移到柱子C
n=int(input("盘子的数量为 "))
def move(n, A, B, C):
     if n==1:
          print ("move from", A, "to", C)
     else:
          move(n-1, A, C, B)
          move(1, A, B, C)
          move(n-1, B, A, C)
print(move(n, "A", "B", "C"))