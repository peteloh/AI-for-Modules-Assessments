#TaskB my CID 01742057
import math
a = 0
def mySum(n,i):
    if i == n:
        return ((i**a))/math.factorial(i-1)
    return ((i**a)/ math.factorial(i-1)) + mySum(n,i+1)
print(mySum(15,1))
    