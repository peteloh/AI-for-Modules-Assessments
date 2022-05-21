#recursive function
def Factorial(N):
    # this function computes the factorial of n
    Rf = range(1,N+1)
    f = 1
    for i in Rf:
        f = f * i
    return f


def sum_S(N,a):
    for i in range(1,N):
        s=0
        if N==1:
            sum+= i**a
        else:
            sum+=  i**a/Factorial(i-1) + sum_S(N-1,a) #recursive function
        return sum


N=15    
a=0
Factorial(15)
sum_S(15,0)