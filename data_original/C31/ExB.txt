#01779587

#importing libraries
import random as rd
import math as mt
import matplotlib.pyplot as pl

#plot the bounding circles 
Rtheta = range (0,360)
for theta in Rtheta: 
    thetar = theta * mt.pi / 180
    pl.scatter(10*mt.cos(thetar), 10*mt.sin(thetar), s = 3, c  = 'b')
    pl.scatter(20*mt.cos(thetar), 20*mt.sin(thetar), s = 3, c  = 'b')
pl.axes().set_aspect('equal')


#plot initial position of ant 
r = rd.random()
theta = rd.random()*2*mt.pi
x = 0
y = 18
pl.scatter(x,y)

#move the points N times
# 5th digit is 9, 7th digit is 8
s1 = 1.8
s2 = 1.4
Rn = range(1,N+1)
while i in y>0: 
    #store the current position as the previous one
    #this is needed as we want to plot the move from a to b as a line 
    xp = x
    yp = y 
    dx = rd.randint(-1.8,1.8)
    dy = rd.randint(-1.4,1.4)
    #do the move, update the coordinates of the ant
    x += dx
    y += dy
    #check if the ant goes outside the boundary 
    if (x**2+y**2)>400 or (x**2+y**2)<100:
        #bring it back to where it was 
        x -= dx
        y -+ dy 
    #plot the current position 
    pl.plot([xp,x],[yp,y],c='Red')
    