#CID = 01712921





s1 = (2/10)+0.9
s2 = (2/10)+0.6
#s1 = 1.1
#s2 = 0.8


#import the required libraries as shortcuts
import math as mt
import random as rd
import matplotlib.pyplot as pl

# Number of possible moves
N = 100000

# plot the donut shape
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),s=3,c='b')
pl.axes().set_aspect('equal')  
 
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * mt.pi / 180
    pl.scatter(10*mt.cos(thetar),10*mt.sin(thetar),s=3,c='b')
pl.axes().set_aspect('equal')  

#plot the starting position
x = 0
y = 18
pl.scatter(x,y)

# move the point 
Rn = range(1,N+1)
for i in Rn:
    # have to store the current position as previous one in order to plot
    xp = x
    yp = y
    # calculate the size of the move, dx, dy using my s1 and s2 from CID values
    dx = (rd.random()*1.9-1.1)
    dy = (rd.random()*1.9-1.1)

# move the ant and then update the coordinates of the ant
    x += dx
    y += dy
    # this checks if the ant goes outside the boundary (crashed into the donut)
    if (x**2+y**2)>400 or (x**2+y**2)<100 : 
    # if it crashes, take it back to previous position
        x -= dx
        y -= dy 
    if y <= 0:
        break
        # plot the path of the ant moving
    pl.plot([xp,x],[yp,y],c='Red')






















