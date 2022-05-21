# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:36:56 2020


"""
#CID: 01759172

#6th digit of CID is 1S
a = 1

#n! function
def Factorial(n):
    #number from 1 to n
    Rf = range(1,n+1)
    f = 1
    for i in Rf:
        f = f * i
    return f

def Sum(N):
    if N == 1:
        S = 1
    else:
        S = N**a/Factorial(N-1) + Sum(N-1)
    return S

#example
N=15
b = Sum(N)
print(b)
    