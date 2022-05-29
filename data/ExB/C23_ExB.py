#01703867
import math as mt # import required libraries
import random as rd
import matplotlib.pyplot as pl

s1=(3/10)+0.9 # work out s1 and s2 values
s2=(6/10)+0.6
Rtheta=range(0,360) # plot circle, set theta value
for theta in Rtheta:
    thetar=theta * mt.pi/180
    pl.scatter(10*mt.cos(thetar),10*mt.sin(thetar),c='b') # plot inner circle
    pl.scatter(20*mt.cos(thetar),20*mt.sin(thetar),c='b') # plot outer circle
    pl.axes().set_aspect('equal') # set axis equal - looks better
x=0 # set intial coordinates of ant
y=18
pl.scatter(x,y) # plot point
N=200 # set arbitary amount of moves
R=range(1,N+1)
for i in R:
    xp=x # store current position as previous one
    yp=y
    dx=rd.random()*(2*s1)-s2 # compute size of dx and dy
    dy=rd.random()*(2*s1)-s2
    x+=dx # update coordinates of ant
    y+=dy
    if (x**2+y**2)>=20 or (x**2+y**2)<=10: # if ant touches wall it bounces off
        x-=dx
        y-=dy
    if y<=0: # if ant goes below x axis it has escaped
        print('Ant escapes!')
    pl.plot([xp,x],[yp,y],c='r')# plot trace