

import random
import math
import matplotlib.pyplot as plt

def randomStep():
    cid = '01704452'
    s1 = (float(cid[4])/10.0) + 0.9
    s2 = (float(cid[6])/10.0) + 0.6
    dx = random.uniform(-s1, s2)
    dy = random.uniform(-s1, s2)
    return dx, dy

def distance(x, y):
    return math.sqrt(x**2 + y**2)

def simulate(start_x, start_y):
    step = 0
    pos_x = []
    pos_y = []
    x, y = start_x, start_y
    print(step, x, y)
    step +=1
    while(y >= 0):
        dx, dy = randomStep()
        new_pos = distance(x + dx, y + dy)
        if new_pos >= 10 and new_pos <= 20:
            x, y = x+dx, y+dy
        print(step, x, y)
        pos_x.append(x)
        pos_y.append(y)
        step +=1

    return pos_x, pos_y

X, Y = simulate(0, 18)
plt.scatter(X, Y)
plt.show()
#CID - 01704452