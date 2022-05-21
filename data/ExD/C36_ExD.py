# 6th digit of CID is 1

a = 1

def Fac(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return(f)

def SUM(N):
    S = 0
    for i in range(1,N+1):
        S = S + i**a/(Fac(i-1))
    return S

SUM(15)