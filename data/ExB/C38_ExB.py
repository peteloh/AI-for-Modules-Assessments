#CID:01702139
import math as mt               #import necessary libraries
import random as rn
import matplotlib.pyplot as plt

s1=(1/10)+0.9                  #Find s1 and s2 using my CID
s2=(9/10)+0.6
dx=(-s1)+rn.random()*(s2+s1)

dy=(-s1)+rn.random()*(s2+s1)    #Find dx and dy, using the random function.   
print(dx,dy)

x=0         #starting point
y=18
steps=0    #Number of steps initialised
if (x+dx)**2+(y+dy)**2<20**2 and (x+dx)**2+(y+dy)**2>10**2:
    steps=steps+1           #If motion is within the 2 circles, dx and dy are added to starting position.
    x=x+dx             #if successful number of steps increases     
    y+y+dy
else:
    x=x+0            #if motion is not within the area specified, x and y remain the same.
    y=y+0 
print(x,y)

plt.scatter(x,y)     #plotting the  value of x and y.

    