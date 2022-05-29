def transpose(A):
    #Function finds transpose of a matrix
    M = len(A)      # Number of rows of A
    N = len(A[0])   # Number of columns
    matrix = []
    for row in range(0, N):                     # Iterating through the rows
        transposedrow = []                      # Creating the row in the transposed matrix
        for column in range(0, M):              # Iterating through the elements in the matrix
            transposedrow += [A[column][row]]   # Adding elements in the transposed matrix
        matrix += [transposedrow]
    return matrix

def matrixaddition(A, transA):
    # Function addds two matrices together
    M = len(A)      # Number of rows of A
    N = len(A[0])   # Number of columns
    matrix = []
    for row in range(0, N):                     # Iterating through the rows
        addedrow = []
        for column in range(0,M):
            addedrow += [A[row][column] - transA[row][column]]
        matrix += [addedrow]
    return matrix

def MatVec(matrixsubtract, b):
    # Function computes the matrix vector multiplication between A and b
    c = []
    sum = 0
    N = len(A) # Number of rows
    M = len(A[0]) #Number of columns
    if M == len(b):
        for i in range(0, N): #Going through rows
            sum = 0
            for j in range(0, M): # Going through columns
                sum += matrixsubtract[i][j] * b[j]      # Vector dot product calculation for the sum, in each row
            c += [sum]
    else:
        c = 0
    return c

def matrixA(n): # Making the matrix a
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)

    for i in range(1, n):
        matrix[i][i] = i + 1
        matrix[i][n-1-i] = i + 1
        
    return matrix

# Putting all functions inside one function
def c_calc(A, b):
    a_trans = transpose(A)
    subtracted_matrix = matrixaddition(A, a_trans)
    return MatVec(subtracted_matrix, b)


A = matrixA(8)
b = [0, 1, 7, 0, 3, 0, 8, 7]

c = c_calc(A, b)
