#CID:01701263

#TaskB
import math as mt
import matplotlib.pyplot as pl
import random as rn

CID=[0,1,7,0,1,2,6,3]
fth=CID[5-1]
sth=CID[7-1]
#print(fth,sth)

s1=(fth/10)+0.9
s2=(sth/10)+0.6

r=0.01 #Plot the point
Rtheta = range(0,360)
for theta in Rtheta:
    theta = theta * mt.pi / 180
    pl.scatter(r*mt.cos(theta),r*mt.sin(theta)+18,s=1,c='r')
#pl.axes().set_aspect('equal') 

r=20 #Plot the big circle
Rtheta = range(0,360)
for theta in Rtheta:
    theta = theta * mt.pi / 180
    pl.scatter(r*mt.cos(theta),r*mt.sin(theta),s=1,c='b')
#pl.axes().set_aspect('equal')  

r=10 #Plot the smaller circle
Rtheta = range(0,360)
for theta in Rtheta:
    theta = theta * mt.pi / 180
    pl.scatter(r*mt.cos(theta),r*mt.sin(theta),s=1,c='b')
#pl.axes().set_aspect('equal') 

#Original point
x=0
y=18

success=False
while not success:
    xp=x #keep updating the previous x
    yp=y #keep updating the previous y
    dx = rn.random()*(s2+s1)-s1
    dy = rn.random()*(s2+s1)-s1
    x+=dx
    y+=dy
    if (x**2+y**2)>20**2 or (x**2+y**2)<10**2: #if touch the boundary
        x -= dx #move backwards
        y -= dy #move backwards
    if y<0:
        success=True

    pl.plot([xp,x],[yp,y],c='g')
