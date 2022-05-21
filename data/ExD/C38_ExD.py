#CID:01702139
import math as mt
def Sum(N):      #setting up the function
    a=3          #6th digit of CID
    if N==1:     #When N=1 it is a special case, so it is defined separately.
        S=1**a
    else:
        S=(N**a)/mt.factorial(N-1)+Sum(N-1) #For other N, function calculates S for that specific N, and recalls itself to find the total S, by adding current S to previous S.
                                             
    return S                  

A=Sum(3)
print(A)


    