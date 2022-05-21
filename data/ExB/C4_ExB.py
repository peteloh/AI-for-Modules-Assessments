import math as mt
import random as r
import matplotlib.pyplot as pl



# plot the bounding circle
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),s=3,c='b')
    pl.scatter(10*mt.cos(thetar),10*mt.sin(thetar),s=3,c='b')
pl.axes().set_aspect('equal')   

x = 0
y = 18
pl.scatter(x,y)

# move the point large number times
Rn = range(1,1000)
for i in Rn:
    # store the current position as previous one
    # this is needed as we want to plot the move from a to b as a line
    xp = x
    yp = y
    #size of the move, dx, dy
    dx = r.uniform(-1.5,1.4)
    dy = r.uniform(-1.5,1.4)
    # do the move: update the coordinates of the ant
    x += dx
    y += dy
    # check if the ant goes outside the boundary
    if (x**2+y**2)>20 or (x**2+y**2)<10:
        # if so, bring it back where it was
        x -= dx
        y -= dy 
    # plot current position
    pl.plot([xp,x],[yp,y])
    #When the ant reaches the boundary break the sequence
    if y<0:
        break

