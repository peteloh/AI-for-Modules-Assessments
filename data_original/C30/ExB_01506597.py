# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:57:17 2020

"""


# CID: 01506597


import random as rn


# for me, s1 and s2 are:
s1=(6/10)+0.9
# s1=1.5

s2=(9/10)+0.6
# s2=1.5

# these two lists will plot the position of the ant, starting at the initial point
x=[0]
y=[18]

i=0
# this condition checks whether the last element of x is negative, if so the ant is in the green part and the code stops
while x[len(x)-1]>0:
    # dx and dy are random numbers between -s1 and s2. their lowest value possible is -s1, and they have a range of (s2-(-s1))
    dx=-s1+rn.random()*(s2-(-s1))
    dy=-s1+rn.random()*(s2-(-s1))
    x=x+[x[len(x)-1]+dx]
    y=y+[y[len(y)-1]+dy]
    # this next line checks if the latest point is in the circle
    if (x[len(x)-1])**2+(y[len(y)-1])**2>=20**2 or (x[len(x)-1])**2+(y[len(y)-1])**2<=10**2:
        x=x-[x[len(x)-1]]
        y=y-[y[len(y)-1]]
        i=i+1
    else:
        i=i+1


import matplotlib.pyplot as plt

# this plots the points
plt.scatter(x,y)