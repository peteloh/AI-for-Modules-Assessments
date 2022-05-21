#01718219

import math

#6th digit of CID = 2

def Sum(n):
    if n==1:
        #define finishing itertion to not cause infinite loop
        S = 1
    else:
        #add final to previous sums
        S = n**2/math.factorial(n-1) + Sum(n-1)
    return S

#test
Sum(5)