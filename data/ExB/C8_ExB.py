# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:16:12 2020


"""
"""CID 01726586"""
import math as mt
import matplotlib.pyplot as plt
import random as rn 

CID=[0,1,7,2,6,5,8,6]
s1=(CID[4]/10)+0.9
s2=(CID[6]/10)+0.6

Rin=10 #hole radius
Rout=20 #donut radius
x0=0 #initial coordinates
y0=18

#plot the donut
for theta in range(0,360):
    theta = theta * mt.pi / 180
    plt.scatter(Rout*mt.cos(theta),Rout*mt.sin(theta),s=3,c='b')
    plt.scatter(Rin*mt.cos(theta),Rin*mt.sin(theta),s=3,c='r')
plt.axes().set_aspect('equal')   
    
#ant escapes when theta is bigger than 180 and it is within the radii
#find random values between s1 and s2
disrange=s2+s1
lowerbound=-s1
upperbound=s2
dx=rn.random()*disrange #random movement within values of s1 and s2
dy=rn.random()*disrange

N=0 #number of moves
angle=90
while angle<180:
    x=x0+dx
    y=y0+dy
    angle=mt.acos(x/Rout)
    N+=1 
    # check if the ant goes outside the boundary
    if (x**2+y**2)>20**2 or (x**2+y**2)<Rin**2:
        # if so, bring it back where it was
        x -= dx
        y -= dy 

print(N)
  



