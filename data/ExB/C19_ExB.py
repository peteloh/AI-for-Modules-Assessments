#01730474
import math as mt
import random as rd
import matplotlib.pyplot as pl

# plot the bounding circles
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),s=3,c='b')
    pl.scatter(10*mt.cos(thetar),10*mt.sin(thetar),s=3,c='b')
pl.axes().set_aspect('equal')   
# generate point (0,18)
x = 0
y = 18
pl.scatter(x,y)

Rn = range(1,N)
for i in Rn:
    # store the current position as previous one
    # this is needed as we want to plot the move from a to b as a line
    xp = x
    yp = y
    # compute the size of the move, dx, dy, s1=-0.9, s2=1.3
    dx = rd.random()*2.4-0.9
    dy = rd.random()*2.4-0.9
    # do the move: update the coordinates of the ant
    x += dx
    y += dy
    # check if the ant goes outside the boundary
    if (x**2+y**2)>400 or (x**2+y**2)<100:
        # if so, bring it back where it was
        x -= dx
        y -= dy 
    if y < 0:
        print("Ant made it yay!")
    # plot current position
    pl.plot([xp,x],[yp,y],c='Red')
