#01718219

import matplotlib.pyplot as plt
import random
import math


CID = [0,1,7,1,8,2,1,9]
#5th digit of CID = 8
#7th digit of CID = 1

#circle bounds
#x**2 + y**2 > 10**2 for inner circle
#x**2 + y**2 < 20**2 for outer circle

#generation of circle
#inner
for theta in range(0,360):
    thetaradian  = theta * (math.pi/180)
    plt.scatter(math.cos(thetaradian)*10,math.sin(thetaradian)*10,s=0.8,c='b')
#outer
for theta in range(0,360):
    thetaradian  = theta * (math.pi/180)
    plt.scatter(math.cos(thetaradian)*20,math.sin(thetaradian)*20,s=0.8,c='r')


plt.axes().set_aspect('equal')


#initial position:
xstart = 0
ystart = 18


#random positioning
s1 = 8/10 + 0.9
s2 = 1/10 + 0.9
dx = random.uniform(-s1,s2)
dy = random.uniform(-s1,s2)


#moveforward code
Moveforward = True
if y<0:
    Moveforward = False
else:
    xprev = x
    yprev = y
    x = x + dx
    y = y + dy
    if (x**2 + y**2) > 20**2 or (x**2 + y**2) < 10**2:
        x = xprev
        y = yprev
    plt.plot([xprev,x],[yprev,y])
    
    
    