#CID:01701263

#01720430
#TaskD
import math as mt

CID=[0,1,7,0,1,2,6,3] #CID
a=CID[6-1] 

def Sum(n):
    n-1!=0
    if n==1:
        S=1
    else:
        S=n**a/(mt.factorial(n-1))+Sum(n-1) #Apply recursion
    return S
n=15
S=Sum(n)
print(S)
