#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:24:33 2020

"""

# CID: 01720439

def MatVec(a,b):    #defining function with input a and b
    
    final = []  #empty function that will be filled out
    for i in range (0, 8): #since there will be 8 rows as output c has dimensions (8x1)
        Sum = 0 #initializing the sum
        for j in range(0, 8):   #second loop that will loop 8 times, as b has 8 numbers in the column
            Sum += (a[i][j]-a[j][i])*b[j]   #calculates a-at (as if a = a(ij), aT = a(ji)). Multiplies result with b
        final += [Sum]  #putting the sum into the final vector output
        
    return final#function output

A = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,2,2,0,0,0],[0,0,0,0,0,0,0,0],[0,0,4,0,0,4,0,0],[0,3,0,0,0,0,3,0],[9,0,0,0,0,0,0,9]] #Test function A
B = [0,1,7,2,0,4,3,9] #Test function B

print(MatVec(A,B)) #output printed
