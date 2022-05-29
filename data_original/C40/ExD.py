#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:46:48 2020

"""

# CID: 01720439
import math #required for factorial function
# a = 4

def Sumn(n): #defining recursive function
    if n == 1: #final sumation when n = 1
        Sum = 1 #defining end case.
    else:
        Sum = (n**4)/math.factorial(n-1) + Sumn(n-1) #performs the calculation and invokes addition of sum for lower n's
    return Sum #Sum total of recursively computed values

N = 15 #test case

print(Sumn(N)) #printing test case