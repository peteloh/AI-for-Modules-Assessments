# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:34:51 2020


"""
#CID: 01759172

#Matrix transposed function
def Transpose(A):
    # find size of A
    M = len(A) # number of rows
    N = len(A[0]) # number of column
    RM = range(0,M)
    RN = range(0,N)
    T = []
    for i in RN:
        row = []
        for j in RM:
            row += [A[j][i]]
        T += [row]
    return T

#A.b function
def MatVec(A,b):


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

#Matrix A
A = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,5,5,0,0,0],[0,0,0,9,9,0,0,0],[0,0,1,0,0,1,0,0],[0,7,0,0,0,0,7,0],[2,0,0,0,0,0,0,2]]


#Matrix b
b = [0,1,7,5,9,1,7,2]


#Transpose A
AT = Transpose(A)

#let d = (A-AT)
# compute d = A - AT
d = [] # initialise d
N=8
RN = range(0,N)
for i in RN:
    # compute row i
    row = [] # initialise row i
    for j in RN:
        # compute column j in row i
        row += [A[i][j] - AT[i][j]]
    # add row i to matrix C
    d += [row]
    
#c=(A-Transpose(A)).b

c = MatVec(d,b)

for row in c:
    print(row)
