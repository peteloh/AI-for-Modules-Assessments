#CID:01713254
def Factorial(n):
    # this function computes the factorial of n
    Rf = range(1,n+1)
    f = 1
    for i in Rf:
        f = f * i
    return f
def S(a,N):
    if N==1:
        s=1
    else:
        s=S(a,N-1)*(((N-1)**2/N)**a)*(N-1)/f(N-2)
    return s
a=2
N=15
S(a,N)
    