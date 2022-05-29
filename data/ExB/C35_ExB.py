#CID:01713254
import matplotlib.pyplot as plt
import math as mt
import random
#Plot the upper half of the doughnut
x=[]
y=[]
for j in range(10,21,10):
    for i in range(0,180):
        x+=[j*mt.cos(i*mt.pi/180)]
        y+=[j*mt.sin(i*mt.pi/180)]
    plt.scatter(x,y)
#Plot the initial position of the ant
x0=[0]
y0=[18]
plt.scatter(x0,y0,c='Blue')
#Calculate s1,s2
s1=3/10+0.9
s2=5/10+0.6
xp=random.uniform(-s1,s2)
yp=random.uniform(-s1,s2)
#xp,yp are the steps the ant jumps
b=1
x=[0]
y=[18]
while y[b-1]>=0:
    if (x[b-1])**2+(y[b-1])**2>10**2 and (x[b-1])**2+(y[b-1])**2<20**2 and y[b-1]!=0:
        #within the doughnut
        x+=[x[b-1]+xp]
        y+=[y[b-1]+yp]
    else:
        #touch the wall or out of the doughnut
        x+=[x[b-1]]
        y+=[y[b-1]]
        #the position is unchanged
    b+=1
plt.scatter(x,y)
plt.show()
    