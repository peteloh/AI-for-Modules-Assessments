#CID01719854
#import any libraries
import math as mt
import random as rd
import matplotlib.pyplot as pl
#plot the bound it moves in
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    pl.scatter(10*mt.cos(thetar),10*mt.sin(thetar),s=1,c='b')
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),s=1,c='b')
pl.axes().set_aspect('equal')  
#plot the starting point
x=0 
y=18
pl.scatter(x,y)
#Creating s1 and s2
S1=(9/10)+0.9
S2=(5/10)+0.6
N=10
# move the point N times
Rn = range(1,N+1)
for i in Rn:
    # store the current position as previous one
    # this is needed as we want to plot the move from a to b as a line
    xp = x
    yp = y
    # compute the size of the move, dx, dy
    dx = (rd.random()*S2)-S1
    dy = (rd.random()*S2)-S1
    # do th emove: update the coordinates of the ant
    x += dx
    y += dy
    # check if the ant goes outside the boundary
    if (x**2+y**2)>20 or (x**2+y**2)<10:
        # if so, bring it back where it was
        x -= dx
        y -= dy 
    # plot current position
    pl.plot([xp,x],[yp,y],c='Red')
print(dx)
print(dy)