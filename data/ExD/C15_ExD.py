#Process: 
#1) need to define a function that computes the factorial of (N-1)
#Here N = 15, but otherwise a userinput for N could be used instead
#2) define a function that will perform the sum up all the values downwards from N using the formula given in the question
#3) the function will only stop when N = 1, as (1-1)! is 0, invalid
#4) the function will recall itself in the loop for N-1 each time, until N ==1 is reached


#6th digit of CID = 9
a = 9
N = 15

#factorial function up to N-1
def factorial(N):
    Rf = range(1,N+1)
    f = 1
    for i in Rf:
        f = f * i
    return f

n = int(input('Gimme a number: '))
res = factorial(N)
print(res)
    
def S(N):
    sum = 0 
    if N == 0: 
        print(sum)
  
    else:
        print(N)
        sum = sum + (N**a)/factorial(N)
        S(N-1)
S(N)

