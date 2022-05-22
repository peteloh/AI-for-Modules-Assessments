#01495089
import math as mt
import random as rd
import matplotlib.pyplot as pl

# set the number of moves
N = 150

# plot the bounding donut
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),s=3,c='b')
pl.axes().set_aspect('equal')   

# generate a random point in the given domain and plot it
#initial location of the ant
x = 0
y = 18
pl.scatter(x,y)

# move the point N times
Rn = range(1,N+1)
for i in Rn:
    # store teh current position as previous one
    # this is needed as we want to plot the move from a to b as a line
    xp = x
    yp = y
    # compute the size of the move, dx, dy
    dx = rd.random()*2.8-1.4
    dy = rd.random()*2.8-1.4
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
    
