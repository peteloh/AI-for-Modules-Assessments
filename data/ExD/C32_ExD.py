#01702538


def factorial(n):
    #check for integer
    if (n%1) != 0:
        return 'Enter integer!'
    #check for number less than 0
    if n < 0:
        return 'Enter number equal to or greater than 0'
    #special condition for n = 0,1
    elif n == 0 or n ==1:
        return 1
    else:
        #apply recursive formula to multiply by previous values of n
        return n*factorial(n-1)

def function(N):
    a = 5
    S = 0
    #check if N given is in region stated
    if N < 1:
        print('Try a different N.')
    #Use 1 known value to end recursive loop
    elif N == 1:
        S = 1
    else:
        #apply recursive formula
        S = N**a / factorial(N-1) + function(N-1)
    
    return S
    
#print(function(4))