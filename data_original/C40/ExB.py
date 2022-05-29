#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:46:19 2020


"""

# CID: 01720439

import math
import matplotlib.pyplot as plt
import random as rn

# s1=0.9, s2 = 0.9

 #Setting axis limits

x = [0]
y = [18]

steps = 0 #initializing a counter

while y[steps]>0: #ie while above x axis
    
    dx = (rn.random()*1.8)-0.9 #defining steps
    dy = (rn.random()*1.8)-0.9
    
    xnew = x[steps]+dx #modelling a step and adding to position array
    ynew = y[steps]+dy
    
    circle = ((xnew)**2) + ((ynew)**2) #circlular position
    ri2 = (10**2) #inner radius square
    ro2 = (20**2) # outer radius squared
    
    if circle > ri2 and circle < ro2: #checks if within boundaries using X^2+y^2=r^2
        x += [xnew]
        y += [ynew]
    else:
        x += [x[steps]]
        y += [y[steps]]
        
    steps += 1
    
plt.axis = ([-21,21,-21,21])
plt.plot(x,y)

print("Steps taken:" + str(steps))