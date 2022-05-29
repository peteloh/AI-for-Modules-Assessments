#Import the libraries
import math as mt
import matplotlib.pyplot as pl
import random

#Calculate s1 and s2
s1 = 3/10 + 0.9
print('S1 is', s1)

#Assign negative value of s1 to another variable
s11 = -s1

s2 = 5/10 +0.6
print('S2 is', s2)

#Produce 2 random numbers (shown bewteen s11 and s2)
def range(s11,s2):
    return random.random() * (s2 + s1) - s1

dx = range(s11,s2)
print('dx is', dx)

dy = range(s11,s2)
print('dy is', dy)

#Create a grid to show the doughnut
pl.axis([-10,10,-20,20])

#Set up starting point of ant
xp = 0
yp =18

#Work out path of ant by addidng dx and dy to starting point of x and y respectively

