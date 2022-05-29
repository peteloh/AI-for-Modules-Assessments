#CID 01719854
#write recursive function to replicate function shown
def Sum(N):
    a=8
    S=1
    if N>1:
        R=range(1,N)
        f=1
        for i in R:
            f=f*i
        S=(N**a)/f + Sum(N-1)
        N=N-1
    else:
        return S
    return S
#set N=15
P=Sum(15)
print(P)
