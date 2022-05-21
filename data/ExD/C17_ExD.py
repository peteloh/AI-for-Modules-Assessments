# CID: 01710404

import math as mt

def Sum(N):
    if N == 1: #a way to stop the function continuing forever
        S = 1
    else:
        S = (N)**4 / mt.factorial(N-1) + Sum(N-1) #making a recursive function to add the last element to the newest function with the current number
    return S

#
a = Sum(15)
print(a)