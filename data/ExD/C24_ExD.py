# Solution for Task D
# My CID Number: 01366896

import math as mt

# Recursive function for summation function
def SumS(N):
    a = 8 # 6th digit of my CID number
    
    # initial term of the series
    if N == 1:
        S = 1 # 1^8 / (0!) = 1
    else:
        # sum of the current term and previous term
        S = (N)**a/mt.factorial(N-1) + SumS(N-1)
    return S

# 

# Test the function for N = 15
res = SumS(15)
print(res)