B =[[0],[1],[7],[0],[2],[8],[6],[8]]

RN = range(0,8)
A = [] # initialise the matrix as a list
for i in RN:
    # form i-th row
    row = [] # initialise i-th row as a list
    for j in RN:
        # add j-th column into i-th row
        if j == i or j == 8-1-i:
            row += B[j]
        else:
            row += [0]
    # add row i-th to the matrix A
    A += [row]

#for row in A:
#    print(row) 
    

#B IS A M X 1 MATRIX
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
                sum += int(A[i][j]) * int(b[j])
            c += [sum]
    else:
        # dimensions are not compatible, return the value of zero
        c = 0
        
    return c

T = []
for i in RN:
    row = []
    for j in RN:
        row += [A[j][i]]
    T += [row]
    
#print()
#for row in T:
#    print (row)
    
#have got them mixed up so will use T as the original and A as the transpose

#Minus is A - AT
Minus = []
for i in RN:
    row = []
    for j in RN:
        row += [T[i][j] - A[i][j]]
    Minus += [row]

for row in Minus:
    print (row)
    
c = MatVec(Minus,B)
print(c)