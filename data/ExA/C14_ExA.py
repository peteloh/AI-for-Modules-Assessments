# start by stating my CID for the examiner, which I shall do while assigning it to a variable as a string
cid = '01501086'

print(cid)

# Task A

# each sublist within a matrix list is a row, so a matrix should be referenced Matrix[row, column]

# define a function for computing the transpose of a matrix

def matrixTranspose(A):
    AT = []
    for j in range(0, len(A[0])):
        rowT = []
        for row in A:
            rowT += [row[j]]
        AT += [rowT]
    print('printing transpose of the input matrix')
    print(AT)
    return AT

# define a function for subtracting one matrix from another (A - B)

def matrixSubtract(A,B):
    result = []
    for i in range(0,len(A)):
        row = []
        for j in range(0,len(A[0])):
            row += [A[i][j]-B[i][j]]
        result += [row]
    print('printing the result of first input matrix subtract second input matrix')
    print(result)
    return result

# define a function for multiplying a matrix by a vector (assuming the two are conformable for multiplication)

def matrixVectorMultiply(matrix,vector):
    result = []
    for i in range(0, len(vector)):
        element = 0
        for j in range(0, len(vector)):
            element += (matrix[i][j] * vector[j][0])
        result += [element]
    print('printing the product of the matrix and vector')
    print(result)
    return result

# having defined my functions, I'll now define my variables

A = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,5,0,0,5,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,8,0,0,0,0,8,0],[6,0,0,0,0,0,0,6]]
b = [[0],[1],[5],[0],[1],[0],[8],[6]]

# and then finally I'll use those variables as the inputs for my functions

c = matrixVectorMultiply(matrixSubtract(A,matrixTranspose(A)),b)
print('printing c')
print(c)