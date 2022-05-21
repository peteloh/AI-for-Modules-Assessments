#01703967
N=int(input('Enter number: ')) # Let user choose number
def Factorial(N): # First makr factorial fucntion to use in recursive function
    r=range(1,N) # range is (1,N), not (1,N+1)-as factorial is (i-1)! not (i)!
    F=1 # when N is 1, factorial is 1
    for i in r:
        F=F*i
    return F # return function
def RecF(N): # make recursive function
    A=Factorial(N) # let A be the denominator factorial
    if N==1:
        S=1 # when N=1, S=1
    else:
        S=((N**9)/A) + RecF(N-1) # for all other N values - recursive
    return  # return function
a=RecF(N)
print(a)