#CID number : 01773062

import random
import math
import matplotlib.pyplot as pl

#create the boundary first
R = range(0,360)
Radius = 20 #outer radius
Radiusin = 10 #inner radius
for i in R:
    theta = i*math.pi/180
    pl.scatter(Radius*math.cos(theta),Radius*math.sin(theta), s = 3, c="Red")
    pl.scatter(Radiusin*math.cos(theta),Radiusin*math.sin(theta), s = 3, c="Green")
pl.axes().set_aspect('equal') #axes are equal in distance

#plot first point of the ant
x = 0
y = 18

#how many times does the ant move
N = int(input('What is N?'))
#compute movement of the ant
Rn = range(1,N+1)
for i in Rn:
    #have to store current position as previous one
    xp = x
    yp = y
    #compute the size of the first movement 
    # s1 = 0.3+0.9= 1.2 , s2 = 0.6+0.9 = 1.5
    dx = random.random()*2.4-1.2
    dy = random.random()*3.0-1.5
    #compute ant movement
    x += dx
    y += dy
    #if the ant exceeds the boundary, bring it back to its previous position
    if x**2 + y**2 > 20 or x**2 + y**2 < 10 :
        x -= dx
        y -= dy
        #if yp < 0 :
            #break
    pl.plot([xp,x],[yp,y],c='Blue')
    



    