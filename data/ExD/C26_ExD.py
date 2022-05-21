#CID:01730549
def Factorial(N):
    f=1
    for i in range(N,0,-1):
        f=f*i
    return(f)
def S(N):
    a=5 #my 6th number
    if N==1:
        s=1 #1st value of sum when i=1
        s=S(N-1)+i**a/Factorial(N-1)
D=S(15)
print(D)
