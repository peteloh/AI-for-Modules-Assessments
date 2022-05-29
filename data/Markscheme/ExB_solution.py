# Ex 2
import math as mt
import random as rd
import matplotlib.pyplot as pl

# set s1, s2
s1 = b[4]/10+0.9
s2 = b[6]/10+0.6
print(s1,s2)

# plot the doughnut
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    pl.scatter(10*mt.cos(thetar),10*mt.sin(thetar),s=3,c='b')
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),s=3,c='b')
pl.axes().set_aspect('equal')

# set the initial position
xc = 0
yc= 18
pl.scatter(xc,yc,c='r')

# start moving
while yc >=0:
#for i in range(0,800):
    # establish next advancement, dx, dy, independently
    dx = rd.random()*(s2+s1)-s1 # random number between -s1 and s2
    dy = rd.random()*(s2+s1)-s1 # random number between -s1 and s2
    # compute next position
    xn = xc + dx
    yn = yc + dy
    rs = xn**2 + yn**2
    # check if nect position is within doughnut
    if 100<rs<400:
        # the new position is within the doughnut, move the ant
        pl.plot([xc,xn],[yc,yn],c='r')
        xc = xn
        yc = yn

        
        
    