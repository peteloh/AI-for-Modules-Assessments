# CID: 01702304

# define a function to produce (n-1)!
def Factorial(n):
    R = range(1,n)
    x = 1
    for i in R:
        x = x*i
    return x

# Define the recursive function with an exit condition
def Rec(N):
    if N == 1:
        S = 1
    else:
        S = (N**3)/(Factorial(N)) + Rec(N-1) 
    return S

# Test for N = 15
a = Rec(15)
print(a)