#01779587

B = [0,1,7,7,9,5,8,7]

N = 8
RN = range(0,8)
A = [] # initialise the matrix as a list
for i in RN:
    # form i-th row
    row = [] # initialise i-th row as a list
    for j in RN:
        # add j-th column into i-th row
        if j == i or j == N-i-1:
            row += B[j]
        else:
            row += [0]
    # add row i-th to the matrix A
    A += [row]

for row in A:
    print(row)

#creating the transpose 
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

# define a as A - Atransposed
a = (A - Transpose(A))

for i in range(len(b)):
    c = a[i][0]*b[i]
