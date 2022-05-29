import math as mt
import matplotlib.pyplot as pl

f = open('xaxis.txt','r')
t = f.readlines()
f.close()

x = []
for item in t:
    x += [float(item.rstrip())]

N = 10
y = []
for xp in x:
    yp = 0
    for n in range(0,N+1):
        yp += (-1)**n * xp**(2*n) / mt.factorial(2*n+1)
    y += [yp]
pl.scatter(x,y,s=1)
pl.grid()

Nx = len(x)
Rx = range(1,Nx-1)
dy = []
for i in Rx:
    dy += [(y[i+1]-y[i-1])/(x[i+1]-x[i-1])]
    
pl.scatter(x[1:Nx-1],dy,s=1)    