# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:14:30 2016

@author: ericgrimson
"""

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)
printName(lastName="Dufresne", firstName="Will", reverse=False)