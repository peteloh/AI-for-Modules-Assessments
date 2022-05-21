import math as mt
def Rec(N):
    #S is not 0 at N=1 but rather there is no solution
    s=0
    if N==1: 
        S=0
    else:
        S = ((N**7)/mt.factorial(N-1))+Rec(N-1)
    return S+1
print(Rec(15))