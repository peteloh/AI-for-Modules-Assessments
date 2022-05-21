#01730474
def Factorial(n):
    # this function computes the factorial of n
    Rf = range(1,n+1)
    f = 1
    for i in Rf:
        f = f * i
    return f

def Sum(N):
    if N == 1:
        S = 1
    else:
        S = (N**4)/Factorial(N-1) + Sum(N-1)
    return S

a = Sum(int(input("N: ")))
print(a)