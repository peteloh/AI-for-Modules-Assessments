#CID:01730549
import matplotlib.pyplot as plt
import random as r
import math as m
#initially
x=0
y=18
s1=0/10+0.9
s2=4/10+0.6
#hence from (-0.9,1)
exit=False
while(exit==False):
    dx=-abs(r.random())*0.9+abs(r.random())
    #dx and dy are independent with same range
    dy=-abs(r.random())*0.9+abs(r.random())
    x=x+dx
    y=y+dy
    if(x**2+y**2>20**2 or x**2+y**2<10**2):
        x=x-dx
        y=y-dy
    print(y)
    plt.scatter(x,y,s=2,c='black')
    if (y<0):
        exit=True
#This will probably never end since the probability that the net increase of y will be positive is way higher as my 5th number is 0 and dy=(-0.9,1)
