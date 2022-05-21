#CID01719854
#first form the matrices A and B
A=[[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,1,1,0,0,0],[0,0,0,9,9,0,0,0],[0,0,8,0,0,8,0,0],[0,5,0,0,0,0,5,0],[4,0,0,0,0,0,0,4]]
print(A)
#make a function to transpose a matrix A
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
T=Transpose(A)
print(T)
#then take away the transpose of A from A
D = [] # initialise D
N=len(A)
RN = range(0,N)
for i in RN:
    # compute row i
    row = [] # initialise row i
    for j in RN:
        # compute column j in row i
        row += [A[i][j] - T[i][j]]
    # add row i to matrix C
    D += [row]
print(D)
#first form b
b=[[0],[1],[7],[1],[9],[8],[5],[4]]
print(b)
#then write a function to dot D with b
def MatVec(D,b):
    # this function computes the matrix vector multiplication between D and b
    # C = D . b    
    # check if dimensions are compatible
    N = len(D) # number of rows
    M = len(D[0]) # number of columns
    C = []
    RN = range(0,N)
    RM = range(0,M)
    for i in RN:
        # compute c(i)
        sum = 0
        for j in RM:
            sum += D[i][j]*b[j]
        C += [sum]
C=MatVec(D,b)
print(C)







  