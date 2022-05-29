# -*- coding: utf-8 -*-
"""
Question 4 Computing Exam


"""

def factorial(n):
    if n == 0 or n == 1: #These are the boundary conditions when n = 0 and n = 1
        return 1 #0! and 1! = 1
    elif n<0 or type(n) is float: #error checking to make sure the input is a positive integer
        return 'I cant let you do that'
    else:
        return (n*factorial(n-1)) # Recursive part of function that finds the factorial of the number 
#Task D. Change to correct number
def TaskD(n):
    #basic error checking
    if n<1:
        return 'cannot do that'
    if n == 1: #Boundary conditions when n = 1 which is the lower value of the sum
        return (1) # The output when n=1
    else:
        return ((n**(4))/(factorial(n-1)))+TaskD(n-1) #Creates the sum by adding previous recursions until n = 1