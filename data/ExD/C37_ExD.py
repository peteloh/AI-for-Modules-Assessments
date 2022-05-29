import numpy as np
sum = 0
N=15
a=5
x1 = range(N)
q=np.power(x1,a)
for i in range(1, N):
    s = 1
    e = 1
#define variables we need
    for j in range(2, i+1):
        s *= j
#factorial of (n-1)
        p=1/s
        x1 = range(N)
        e=p
#a rewrite of given equation
    sum += e
#the adding up of each term
print(sum)
#print the answer

