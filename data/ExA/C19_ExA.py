#01730474
def Transpose(A):
    # find size of A
    M = len(A) # number of rows
    N = len(A[0]) # number of column
    RM = range(0,M) #traverse rows
    RN = range(0,N) #traverse columns
    T = []
    for i in RN:
        row = []
        for j in RM:
            row += [A[j][i]]
        T += [row]
    return T

def MatMat(A,T,b):
    # this function computes the matrix vector multiplication between (A-T) and b
    # c = (A-T) . b    

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
                sum += (A[i][j] - T[i][j]) * b[j]
            c += [sum]
        return c

N = 8
b = [0,1,7,3,0,4,7,4]
RN = range(0,N)
A = [] # initialise the matrix as a list
for i in RN:
    # form i-th row
    row = [] # initialise i-th row as a list
    for j in RN:
        # add j-th column into i-th row
        if j == i or j == N-i-1:
            row += [b[i]]
        else:
            row += [0]
    # add row i-th to the matrix A
    A += [row]

for row in A:
    print(row)
T = Transpose(A)
for row in T:
    print(row)
c = MatMat(A,T,b)
for row in c:
    print(c)