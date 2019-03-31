#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:28:16 2019

@author: Will
"""

bob=0
s='azcbobobegghakl'
for i in range(len(s)):
     if s[i]=="b" and s[(i+1)]=="o" and s[(i+2)]=="b":
          bob+=1
print(bob)