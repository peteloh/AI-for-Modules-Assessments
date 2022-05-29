# CID: 01720187

# import math as mt
import matplotlib.pyplot as pl
import random as rn
import math


# Initial positions
x = 0
y = 18

s1 = -0.9
s2 = 1.4
ds = s2-s1

xpos = []
ypos = []
trapped = True

while trapped:
    dx = rn.random() * ds + s1
    dy = rn.random() * ds + s1
    xpos += [x]
    ypos += [y]

    # if in circle add dx and dy to x and y
    if 100 < x**2 + y**2 < 400 and y > 0:
        x += dx
        y += dy
    # if out of circles put back to previous spot
    elif (x**2 + y**2 < 100 or x**2 + y**2 > 400) and y > 0:
        x = xpos[-2]
        y = ypos[-2]
    # if below y axis it has escaped
    elif y < 0:
        print("Escaped")
        break


# draw bounding circles
def circle(r, xc, yc):
    # map out polar coordinates
    Rtheta = range(0, 360)
    # for 360 around centre plot points.
    for theta in Rtheta:
        thetar = theta * math.pi / 180
        pl.plot(r * math.cos(thetar) + xc, r * math.sin(thetar) + yc, s=3, c='red', alpha=1)


# Plot circles and positions of ant
circle(10, 0, 0)
circle(20, 0, 0)
pl.plot(xpos, ypos)
pl.show()
