# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:55:22 2020


"""


# CID: 01506597


# I am creating an 8*8 matrix of zeros for matrix A
N=8
A=[]
for i in range(N):
    A=A+[[]]
    for j in range(N):
        A[i]=A[i]+[0]


# this is matrix b
b=[0,1,5,0,6,5,9,7]

# I am creating matrix A by adding my CID to the relevant terms using matrix b
for i in range(len(A)):
    A[i][i]=b[i]
    A[i][-i-1]=b[i]




# I am creating the transpose of A
def transpose(A):
    # First, I am creating an 8*8 matrix of zeros the same size as matrix A
    T=[]
    for i in range(len(A)):
        T=T+[[]]
        for j in range(len(A[0])):
            T[i]=T[i]+[0]
    # Now I am using the terms from matrix A to create the transpose
    for i in range(len(A)):
        for j in range(len(A[0])):
            T[j][i]=A[i][j]
    return T


T=transpose(A)


# d is the matrix formed by (A-Transpose(A))
# first, I am creating an 8*8 matrix of zeros the same size as matrix A
d=[]
for i in range(len(A)):
    d=d+[[]]
    for j in range(len(A[0])):
        d[i]=d[i]+[0]
# Now I am using the terms from matrix A and matrix T to create the d
for i in range(len(A)):
    for j in range(len(A[0])):
        d[i][j]=A[i][j]-T[i][j]


# this function multiplies a matrix and a column vector
def matvec(d,b):
    C=[]
    # first, this checks if the sizes of the matrices are compatible
    if len(b)!=len(d[0]): 
        C=0
        return C
    else:
        # this carries out the multiplication
        for i in range(len(d)):
            c=0
            for j in range(len(b)):
                c=c+d[i][j]*b[j]
            C=C+[c]
        return C

# this calculates matrix c from d and b obtained previously
c=matvec(d,b)
