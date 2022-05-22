# CID: 01702304

#form matrix A
A = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0],[0,0,3,0,0,3,0,0],[0,0,0,0,0,0,0,0],[4,0,0,0,0,0,0,4]]
for row in A:
    print(row)
    
#form matrix B
B = [0,1,7,0,2,3,0,4]
for row in B:
    print(row)
    
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

#main script, read and form matrix AT
AT = Transpose(A)
for row in AT:
    print(row)
    
# compute D = A - AT
D = [] # initialise C
RN = range(0,8)
for i in RN:
    # compute row i
    row = [] # initialise row i
    for j in RN:
        # compute column j in row i
        row += [A[i][j] - AT[i][j]]
    # add row i to matrix C
    D += [row]
print('')
for row in D:
    print(row)
    
def MatVec(D,B):
    # function calculates the matrix vector multiplication between D and B
    # c = D . B    

    # check if dimensions are compatible
    N = len(D) # number of rows
    M = len(D[0]) # number of columns
    # number of columns of A must equal the length of b
    if M == len(B):
        # dimensions are compatible: do the multiplication
        c = []
        RN = range(0,N)
        RM = range(0,M)
        for i in RN:
            # compute c(i)
            sum = 0
            for j in RM:
                sum += D[i][j] * B[i]
            c += [sum]
    else:
        # dimensions are not compatible, return the value of zero
        c = 0
        
    return c
print(B[2])
# main script, form c

c = MatVec(D,B)
print(c)