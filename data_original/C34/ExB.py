# -*- coding: utf-8 -*-
"""
Question 2 Computing Exam


"""
import matplotlib.pyplot as plt
import math
import random

def antgame():
    #calculate s1 and s2
    s1 = (5/10)+0.9
    s2 = (9/10)+0.6
    #current positions. At t=0 x=0 and y=18
    currentx = 0
    currenty = 18
    x_positions = [0]
    y_positions = [18]
    while currenty>0:
        #generates dx and dy
        dx = random.uniform((-s1), (s2))
        dy = random.uniform((-s1), (s2))
        currentx += dx
        currenty += dy
        if (currentx**2+currenty**2)**0.5 <= 10 or (currentx**2+currenty**2)**0.5 > 20: #boundaries of wall using hypotenuse method where 10 and 20 are radii of the outer and inner circles
            #bounce back implemented and currentx and currenty not appended to positions
            currentx -= dx
            currenty -= dy
        else:
            #if the boundaries are not exceeded, the current position is appended to the history of te ants positions
            x_positions.append(currentx)
            y_positions.append(currenty)
    #history of ant positions plotted
    plt.scatter(x_positions, y_positions, color='r', marker = "o", s=1)
    ax = plt.gca()
    #outer and inner circlular boundaries plotted
    innercircle = plt.Circle((0, 0), 10, color='b', fill=False)
    ax.add_artist(innercircle)
    outercircle = plt.Circle((0, 0), 20, color='b', fill=False)
    ax.add_artist(outercircle)
    #make the graph look neat
    ax.set_xlim((-22, 22))
    ax.set_ylim((-22, 22))
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()
        
    
