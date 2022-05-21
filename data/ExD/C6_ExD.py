import math as mt
def Summation(N):
    if N == 1:
        # exit condition
        f = 1
    else:
        # recursive formula
        f = (N**8)/mt.factorial(N-1) + Summation(N-1)
    return f

a = Summation(15)
print(a)