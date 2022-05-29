# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:36:34 2020


"""
"""CID 01726586"""

b=[0,1,7,2,6,5,8,6] #vector b

def transpose(A):
    N=len(A) #number of rows
    M=len(A[0]) #number of columns
    T=[] #initials transpose
    for i in range(0,M):
        row=[]      #no. new rows=no. old columns
        for j in range(0,N):
            row+=[A[j][i]] #swap old rows and columns
        T+=[row] #append new rows
    return T

#subtract 2 square matrices function
def sqsub(A,B): #for A-B
    N=len(A) #it is square so N works for rows and columns of both matrices
    sqsub=[] #initialise result matrix
    for i in range(0,N): #traverse rows
        row=[]
        for j in range(0,N): #traverse columns
            row+=[(A[i][j]-B[i][j])] #subtract b from a
        sqsub+=[row] #append rows
        
    return sqsub

def MatVec(A,b):
    # this function computes the matrix vector multiplication between A and b
    # c = A . b    

    # check if dimensions are compatible
    N = len(A) # number of rows
    M = len(A[0]) # number of columns
    # number of columns of A must equal the length of b
    if M == len(b):
        # dimensions are compatible: do the multiplication
        c = []
        RN = range(0,N)
        RM = range(0,M)
        for i in RN:
            # compute c(i)
            sum = 0
            for j in RM:
                sum += A[i][j] * b[j]
            c += [sum]
    else:
        # dimensions are not compatible, return the value of zero
        c = 0
        
    return c

def c(A,b): #a is matrix, b is vector
    t=transpose(A) 
    f=sqsub(A,t) #subtract transpose of A from A
    c=MatVec(f,b) #multiply subtraction by vector
    return c

#need to make A
N=8 #num of rows and columns
A=[] #initialise A
for i in range(0,N):
    row=[] #form n rows
    for j in range(0,N):
        if i == j or i== N-1-j: 
            row+=[b[i]] #the numberson each row are the row number away from the edge
        else:
            row+=[0] #otherwise its 0
    A+=[row] #append the rows
        
c=c(A,b) #form product c

print(c)













        
            
            
            
            
    
