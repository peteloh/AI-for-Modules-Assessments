
A=[[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,1,1,0,0,0],[0,0,0,6,6,0,0,0],[0,0,7,0,0,7,0,0],[0,8,0,0,0,0,8,0],[2,0,0,0,0,0,0,2]]
B=[[0],[1],[7],[1],[6],[7],[8],[2]]
def Transpose(A):

    # find size of A
    M = len(A) # number of rows
    N = len(A[0]) # number of columns
    RM = range(0,M)
    RN = range(0,N)
    T = []
    for i in RN:
        row = []
        for j in RM:
            row += [A[j][i]]
        T += [row]
    return T

At=Transpose(A)
RN=range(0,len(A))
P1=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
for i in RN:    
# iterate through columns 
    for j in RN: 
        P1[i][j] = A[i][j] - At[i][j] 
#MatMul from previous work

    M = len(P1) # rows of A
    NA = len(P1[0]) # columns of A
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
                    Sum += P1[i][k] * B[k][j]
                row += [Sum] # append this column
            C += [row] # append this row
print(C)
