# CID: 01710404

import random
import matplotlib.pyplot as pl

s1 = 0/10 + 0.9
s2 = 0/10 + 0.6 #calculating s1 and s2

dx = random.uniform(-s1,s2)
dy = random.uniform(-s1,s2)  #calculating dx and dy by finding random number between -0.9 and 0.6

x = [0]
y = [18]   #initial point is (0,18)

while x[-1] > 0 and y[-1] > 0 and x[-1]**2 + y[-1]**2 >= 100 and x[-1]**2 + y[-1]**2 <= 400: #trying to find a condition to stop the function when the point is in the safe zone
    if x[-1]**2 + y[-1]**2 <= 100 or x[-1]**2 + y[-1]**2 >= 400:  #if the point is in the red zone this bounces back to last point
        x = x[-2]
        y = y[-2]
    else:
        x += [x[-1] + dx]  #if not in red zone, another x is added to the list but dx is added and the same for y
        y += [y[-1] + dy]
    
    


print(x)
print(y) 

pl.plot(x,y) #plotting x against y

fig, ax = pl.subplots()

ax.set(xlim=(-21, 21), ylim = (-21, 21))

a_circle = pl.Circle((0, 0), 10)
ax.add_artist(a_circle)

a_circle2 = pl.Circle((0, 0), 20) #plotting the boundary circles
ax.add_artist(a_circle2)