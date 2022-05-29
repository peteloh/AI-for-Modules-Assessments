# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:36:47 2020


"""
#CID: 01759172

import math as mt
import random as rn
import matplotlib.pyplot as pl

#savind file into varible Data
f = open('CV19.txt','r')
Data = f.readlines()
f.close()


N=len(Data)
print(N)

R = range(0,N)
# organise data in a list of tuples
# list of weeks
Weeks = [] 
#intialise position count
c=0
d=3
for i in R:
    while c < len(Data):
        Weeks += [( Data[c].rstrip())]
        c += 15

print(Weeks)