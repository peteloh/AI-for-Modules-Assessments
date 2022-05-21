# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:16:13 2020


"""
"""CID 01726586"""
import math as mt

CID=[0,1,7,2,6,5,8,6]

a=int(CID[5]) #6th difit of CID

def funcS(N,a):
    if N==1:
        S=1 #for i=1 s=1
    else:
        S=((N**a)/mt.factorial(N-1)) + funcS(N-1,a) #otheriwse add the next lower value of i onto it
        
    return S

#test
b=funcS(15,a)
print(b)
        