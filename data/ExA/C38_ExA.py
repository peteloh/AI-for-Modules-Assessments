#CID:01702139
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
a = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0],[0,0,1,0,0,1,0,0],[0,3,0,0,0,0,3,0],[9,0,0,0,0,0,0,9]]
for row in a:
    print(row)
AT=Transpose(a)   #using function above to find AT
for row in AT:
    print(row)

B = [] # initialise B=(A-AT)
RN = range(0,8)
for i in RN:
    # compute row i
    row = [] # initialise row i
    for j in RN:
        # compute column j in row i
        row += [a[i][j] - AT[i][j]]
    # add row i to matrix C
    B += [row]

for row in B:
    print(row)

def Multiply(A,B):
    M = len(A) # rows of A
    NA = len(A[0]) # columns of A
    NB = len(B) # rows of B
    P = len(B[0]) # columns of B
    # define ranges
    RM = range(0,M)
    RN = range(0,NA)
    RP = range(0,P)
    # check that dimensions are compatible
    if NA == NB:
        # compute the product C = A * B
        C = []
        for i in RM:
            # compute row i of the matrix
            row = []
            for j in RP:
                # compute column j, i.e. element C[i][j]
                Sum = 0
                for k in RN:
                    Sum += A[i][k] * B[k][j]
                row += [Sum] # append this column
            C += [row] # append this row
    else:
        # dimensions not compatible
        C = 0
    return C

b=[[0],[1],[7],[0],[2],[1],[3],[9]]
for row in b:
    print(row)
c=Multiply(B,b)
for i in c:
    print(row)