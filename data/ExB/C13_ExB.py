#My CID number is 01700084

import math
import random
import matplotlib.pyplot as pl

CID = [0,1,7,0,0,0,8,4] #this is my CID number

s1 = CID[4]/10 + 0.9 #defining s1
s2 = CID[6]/10 + 0.6 #defining s2

def Ant(a,b):
    x =[]
    y =[]
    xp = 0 #initial position of x and y coordinate
    yp = 18
    Won = False
    while (not Won) and yp >= 0:
        if xp**2 + yp**2 >= 10**2 and xp**2 + yp**2 <= 20**2: #this is to ensure x and y stay within circle
            for i in range(0,len(a)): #showing movement of ant
                dx = a[i]
                dy = b[i]
                xp = xp + dx
                yp = yp + dy
                x = x + [xp]
                y = y + [dy]
        else:
            xp = 0
            yp = 0
            x = x + [xp]
            y = y + [yp]
    if yp < 0: #setting the circumstances where winning is possible
        Won = True
    pl.scatter(x,y) #plotting trace of ant
    pl.axis([-20,20,-20,20])

a = []
b =[]
N = 50
R = range(0,N)


for i in R: 
    dx = random.uniform(-0.9,1.4)
    a = a + [dx]

for j in R:
    dy = random.uniform(-0.9,1.4)
    b = b + [dy]

    #the above was to generate random movement for ant. To make game last longer, change value for n
Ant(a,b)