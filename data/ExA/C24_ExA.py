# Solution for Task A
# My CID Number: 01366896

# Generate a square Matrix A with a the specified configuration with CID number
CID = [0,1,3,6,6,8,9,6]
N = 8 # 8 x 8 Matrix
RN = range(0,N)
A = [] # initialise the matrix as a list
for i in RN:
    # form i-th row
    row = [] # initialise i-th row as a list
    for j in RN:
        # add j-th column into i-th row
        if j == i:
            row += [CID[j]]
        elif j == N-i-1:
            row += [CID[-j-1]]
        else:
            row += [0]
    # add row i-th to the matrix A
    A += [row]

# Find the transpose of A
def TransposeMatrix(m):    
    # Display Matrix m
    print("Matrix:")
    for row in m : 
        print(row) 
    mTranspose = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return mTranspose

AT = TransposeMatrix(A)
print("\nTranspose:")
# Display the transpose of Matrix A
for line in AT:
    print(line)

# Evaluate ASUB = (A - AT)
def MatSubtract(A,B):
    M = len(A) # rows
    NA = len(A[0]) # columns
    # define ranges
    RM = range(0,M)
    RN = range(0,NA)
    C = []
    for i in RM:
        # compute row i of the matrix
        row = []
        for j in RN:
            # compute column j, i.e. element C[i][j]
            row += [A[i][j] - AT[i][j]]
        C += [row] # append this row
    return C

ASUB = MatSubtract(A,AT)
print("\nASUB = (A - AT):")
for line in ASUB:
    print(line)
    
# Compute Matrix multiplication of c = (A - AT)*B
def MatVec(A,b):
    # this function computes the matrix vector multiplication between A and b
    # c = A . b , where A is the matrix and b is the vector
    
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

# Create array B, which is equal to the CID
B = CID
Qn_C = MatVec(ASUB,B)
print("\nC = (A - AT) * B:")
print(Qn_C)