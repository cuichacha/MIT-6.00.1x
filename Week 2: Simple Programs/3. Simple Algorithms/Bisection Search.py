#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:02:16 2019

@author: Will
"""

print("Please think of a number between 0 and 100")
low=0
high=100
while True:
     ans=int((low+high)/2)
     print("Is your secret number",ans,"?")
     print("Enter 'h' to indicate the guess is too high.")
     print("Enter 'l' to indicate the guess is too low.")
     print("Enter 'c' to indicate I guessed correctly.")
     guess=input()
     if guess=="c":
          break
     elif guess=="h":
          high=ans
     elif guess=="l":
          low=ans
     else:
          print("Wrong Input")
print("Game Over")
print("Your secret number was:",ans)