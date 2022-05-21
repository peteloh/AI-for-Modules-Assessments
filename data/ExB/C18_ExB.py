#MEHCH40008

#Computing Exam

#CID: 01704200


#TASK B

#import the necessary libraries
import math as mt
import random as rn
import matplotlib.pyplot as pl
#create a list of your CID number
CID = [0, 1, 7, 0, 4, 2, 0, 0]
#define and plot the outer and inner circles
#create four lists x and y for the point coordinates
xouter = []
youter = []
xinner = []
yinner = []
#traverse all angles from 0 to 2pi in 100 intermediate angles and use polar coordinates to find x and y values for the circles
for i in range(0, 101):
    alpha = 2 * mt.pi * i / 100
    xouter.append(20 * mt.cos(alpha))
    xinner.append(10 * mt.cos(alpha))
    youter.append(20 * mt.sin(alpha))
    yinner.append(10 * mt.sin(alpha))
pl.plot(xinner, yinner, markersize = 2, linewidth = 1, color = 'Blue')
pl.plot(xouter, youter, markersize = 2, linewidth = 1, color = 'Red')
#create the initial position of the ant and a two lists which track the ant's movements
xcurrent = 0
ycurrent = 18
x = []
y = []
#make the ant move until it is in the lower half of the circle ie when ycurrent < 0
while ycurrent > 0:
    #generate the values s1 and s2 between the ant has to move as advised in the task
    s1 = (CID[4] / 10) + 0.9
    s2 = (CID[6] / 10) + 0.6
    #generate the possible movement in the x and y directions between -s1 and s2
    dx = rn.uniform(-s1, s2)
    dy = rn.uniform(-s1, s2)
    #record the current position in the x and y lists
    x.append(xcurrent)
    y.append(ycurrent)
    #create a hypothesis of the new position
    xnew = xcurrent + dx
    ynew = ycurrent + dy
    #if the possible new position is outside of the doughnut, the operation has to be redone
    while xnew ** 2 + ynew ** 2 >= 20 ** 2 or xnew ** 2 + ynew ** 2 <= 10 **2:
        dx = rn.uniform(-s1, s2)
        dy = rn.uniform(-s1, s2)
        xnew = xcurrent + dx
        ynew = ycurrent + dy
    #if inside, the hypothesis becomes the new position
    xcurrent = xnew
    ycurrent = ynew
#append the final position to the list
x.append(xcurrent)
y.append(ycurrent)
#plot the track and the final position
pl.plot(x, y, markersize = 2, linewidth = 1, color = 'Black')
pl.scatter(xcurrent, ycurrent, s = 100, color = 'green', marker = 'x')