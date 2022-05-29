#CID: 01739141
#Task D
def factorial(N):
    if N==1:
        return 1
    else:
        return N * factorial(N-1)
def add(N):
    if N==1:
        S=1
    else:
        S= N**1/factorial(N-1) + add(N-1)
    return S
a= add(15)
print(a)