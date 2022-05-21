# Solution for Task B
# My CID Number: 01366896

import math as mt
import random as rd
import matplotlib.pyplot as pl

# plot the bounding circles
# Radius = 20 (outer circle)
r1 = 20
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    # in the format x = r*cos(thetar)
    pl.scatter(r1*mt.cos(thetar),r1*mt.sin(thetar),s=3,c='b') 
pl.axes().set_aspect('equal')  

# Radius = 10 (inner circle)
r2 = 10
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    # in the format x = r*cos(thetar)
    pl.scatter(r2*mt.cos(thetar),r2*mt.sin(thetar),s=3,c='b') 
pl.axes().set_aspect('equal')  

# generate the initial starting point in the given domain and plot it
xo = 0
yo = 18
x = xo
y = yo
pl.scatter(x,y,s=5,c='Purple')

# Keep moving until the ant exits the doughnut
exit = False
while (not exit):   
    # store the current position as previous one
    # this is needed as we want to plot the move from a to b as a line
    xp = x
    yp = y
    # evaluate s1 and s2 using CID = 01366896
    s1 = 6 / 10 + 0.9
    s2 = 9 / 10 + 0.6
    # compute the size of the move, dx, dy - a number between -s1 and s2 [-1.5,1.5]
    dx = rd.random()*3-1.5
    dy = rd.random()*3-1.5
    # do the move: update the coordinates of the ant
    x += dx
    y += dy
    # check if the ant goes outside the boundary
    if (x**2+y**2)>=20**2 or (x**2+y**2)<=10**2: # equation of a circle
        # if so, bring it back where it was (i.e. undo the move)
        x -= dx
        y -= dy 
    # plot current position - after adjusting if out of bounds
    pl.plot([xp,x],[yp,y],c='Red') # syntax for plotting lines from point 1 [a,b] to point 2 [c,d]
    
    # Exit condition
    if y < 0:
        exit = True