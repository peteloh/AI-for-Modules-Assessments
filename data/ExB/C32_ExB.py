#01702538

import matplotlib.pyplot as plt
import math as m
import random as rn

def Circle(R):
    X = []
    Y = []
    #traverse through full circle
    for i in range(0,360):
        X.append(R*m.cos(m.radians(i)))
        Y.append(R*m.sin(m.radians(i)))
    return (X,Y)
    

def Ant():
    s1 = (2/10)+0.9
    s2 = (2/10)+0.6
    #starting position
    (x,y) = (0,18)
    #Used for trace of ant
    X = [0]
    Y = [18]
    #Will move until reaches bottom half
    move = True
    while move:
        dx = rn.uniform(-s1,s2)
        dy = rn.uniform(-s1,s2)
        #possible new x and possible new y
        xp = x + dx
        yp = y + dy
        #if in red section
        if xp**2 + yp**2 > 10**2 and xp**2 + yp**2 < 20**2 and yp > 0:
            (x,y) = (xp,yp)
            X.append(x)
            Y.append(y)
        #if in green section
        elif xp**2 + yp**2 > 10**2 and xp**2 + yp**2 < 20**2 and yp < 0:
            (x,y) = (xp,yp)
            X.append(x)
            Y.append(y)
            #stop ant
            move = False
        #if outside doughnut
        else:
            #doesn't show bounce back of ant ~ unsure if it is required
            #just returns
            (x,y) = (x,y)
    #Inner circle
    [X1,Y1] = Circle(10)
    plt.plot(X1,Y1,lw=3,c='black')
    #Outer circle
    [X2,Y2] = Circle(20)
    plt.plot(X2,Y2,lw=3,c='black')
    #Middle line
    plt.plot([-20,20],[0,0],lw=1,c='r')
      
    plt.plot(X,Y,c='b',lw=1,label='Ant Movement')
    plt.legend(loc='lower center')
    plt.axis([-20,20,-20,20])
    plt.show()
            
Ant()                
