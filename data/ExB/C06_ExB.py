import math as mt
import random as rd
import matplotlib.pyplot as pl


Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
#    if thetar < mt.pi :
#        Col = 'red'
  #  else:
 #       Col = 'green'
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),s=3,c='r')
    pl.scatter(10*mt.cos(thetar),10*mt.sin(thetar),s=3,c='g')
pl.axes().set_aspect('equal') 

# generate a random point in the given domain and plot it
r = rd.random()*10 +10
theta = rd.random()*2*mt.pi
x = r * mt.cos(theta)
y = r * mt.sin(theta)
pl.scatter(x,y)

# move the point N times
N =100
Rn = range(1,N+1)
for i in Rn:
    xp = x
    yp = y
    # compute the size of the move, dx, dy
    dx = rd.random()*2.3 - 1.1
    dy = rd.random()*2.3 - 1.1
    
    x += dx
    y += dy
    # check if the ant goes outside the boundary
    if (x**2+y**2)>20 or (x**2+y**2)<10:
        # if so, bring it back where it was
        x -= dx
        y -= dy 
    # plot current position
    pl.plot([xp,x],[yp,y],c='Red')