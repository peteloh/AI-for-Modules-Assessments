#01779587
#6th digit is 5

import math as mt 

def Factorial(n):
    # this function computes the factorial of n
    Rf = range(1,n+1)
    f = 1
    for i in Rf:
        f = f * i
    return f
#check factorial function 
n = 15
res = Factorial(n-1)
print(res)

S = 0 
#Evaluate the series 
n = 15 
y = []
Rf = range(1,n+1)
for n in Rf: 
    yp = 0 
    for n in range (0, n+1): 
        yp += n**5 / Factorial(n-1)
        S = S + yp

print (S)
    
