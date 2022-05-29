#CID no : 01773062

import math
import matplotlib.pyplot as pl

#create a recursive function
def Series(x,N):
    Ri = range(1,N+1)
    y = []
    #initial Sum = 0
    Sum = 0
    for xp in x:
        yp = 0
        for i in Ri:
            #add terms up to N
            # 6th digit of CID = 0
            yp += xp**0/math.factorial(xp-1)
        #append this yp
        y += [yp]
        Sum += y
    #return results
    return Sum


N = 15
#create a list of x
x = []
#add items into x
for i in range(1,N+1):
    x += [i]

Sum = 0
#compute y
for i in range(1,N+1):
    Sum += float(y[i])
    #y = Series(x,N)
    #plot the graph
    #pl.plot(x,y)
    print(Sum)
    
