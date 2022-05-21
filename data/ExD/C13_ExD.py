#My CID number is 01700084

import math #so I can use factorial function in math
a = 0 #6th digit of my CID number

N = int(input('Choose a value for N')) #Choosing value for N
S = 0 #Setting initial value for S


for i in range(1,N+1):
    S = S + i**a/math.factorial(i-1)  #the equation I need to find

print(S)   #Result