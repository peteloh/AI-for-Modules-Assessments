# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:36:32 2020


"""
#CID: 01759172

import math as mt
import random as rn
import matplotlib.pyplot as pl

#5th and 7th digits are 9 and 7 respecrively

#s1 = 9/10+0.8
s1 = 1.7
#s2 = 7/10+0.6
s2 = 1.5

#saring position
x = [0]
y = [18]

N=10000
R=(0,N)
for i in R:
    
    #while ant is in the red region, move ant
    while (x[i]**2+y[i]**2>=10 and y[i]>=0) and (x[i]**2+y[i]**2<=20 and y[i]>=0):
    
        #dx and dy are between -1.7 and 1.5
        dx = float(rn.random()*3.2-1.7)
        dy = float(rn.random()*3.2-1.7)
    
        #move ant by dx and dy
        x += [dx]
        y += [dy]
    
        #if ant leaves red region, move to previous poisition
        if (x[i]**2+y[i]**2<=10 and y[i]>=0) and (x[i]**2+y[i]**2>=20 and y[i]>=0):
            x[i] = x[i-1]
            y[i] = y[i-1]
        else:
            pass
        
    pl.scatter(x,y,s=2)
        

#plotting outer and inner circle
circle1 = pl.Circle((0, 0), 20, color='r',fill=False)
circle2 = pl.Circle((0, 0), 10, color='b', fill=False)

# clear graph for fresh plot
ax = pl.gca()
ax.cla() 

# setting range of axis
ax.set_xlim((-20, 20))
ax.set_ylim((-20, 20))

#showing circle
ax.add_artist(circle1)
ax.add_artist(circle2)
    

    

