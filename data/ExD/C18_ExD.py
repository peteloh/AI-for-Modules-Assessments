#MEHCH40008

#Computing Exam

#CID: 01704200


#Question 4

#import the necessary library
import math as mt
#create a list of your CID number
CID = [0, 1, 7, 0, 4, 2, 0, 0]
#find the 6th digit of my CID
a = CID[5]
print(a)
#define a function SUM that given the upper bound of the sum returns its result
def SUM (N):
    #set the value of the sum S if N = 1
    if N == 1:
        S = 1
    #otherwise, find the value of S for the given number and add the value obtained by the function for the precedent N
    else:
        S = ((N ** a) / mt.factorial(N - 1)) + SUM(N - 1)
    #return the value of S
    return S
#check the function for N = 15
print(SUM(15))