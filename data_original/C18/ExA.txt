#MEHCH40008

#Computing Exam

#CID: 01704200


#TASK A

#create a list of your CID number
CID = [0, 1, 7, 0, 4, 2, 0, 0]
#create a matrix A as a list
A = []
#traverse the number of rows of the matrix and create a row list for each
for i in range(0, 8):
    row = []
    #traverse all elements in the row
    for j in range(0, 8):
        #if in the nth row if the element is the nth or last nth(eg 1st row, 1st and last elements), insert the corresponding CID number, otherwise insert 0
        if i == j or i == 7 - j:
            row.append(CID[i])
        else:
            row.append(0)
    #append each row to the matrix list
    A.append(row)
#create a vector b as a list
b = []
for i in CID:
    b.append(i)
#define a matrix which returns the transpose of a matrix
def Transpose (matrix):
    #check whether the matrix is square
    if len(matrix) != len(matrix[0]):
        print('the matrix is not square')
    else:
        #create the resultant matrix
        trans = []
        #traverse the number of rows of the matrix and create a row list for the transpose
        for i in range(0, len(matrix)):
            row = []
            #traverse each row of the matrix and append each element of each column of the matrix to the row of the transpose
            for j in range(0, len(matrix)):
                row.append(matrix[j][i])
            #append each row to the transpose matrix
            trans.append(row)
        return trans
#create the transpose of matrix A
At = Transpose(A)
#define a function which subtracts two matrices
def MatSubtraction (matrix1, matrix2):
    #check whether the two matrices are of the same order
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print('the two matrices are not of the same order')
    else:
        #create a list for the resultant matrix
        res = []
        #traverse the number of rows of both matrices and create a row list for each
        for i in range(0, len(matrix1)):
            row = []
            #traverse the elements in each row of both matrices and append the difference of the corresponding elements to the row list of the resultant matrix
            for j in range(0, len(matrix1[0])):
                row.append(matrix1[i][j] - matrix2[i][j])
            #append each row to the resultant matrix
            res.append(row)
        return res
#compute the matrix D given by the difference between A and At
D = MatSubtraction(A, At)
#define the function which multiplies a matrix by a vector in function of the both
def MatVec(matrix, vector):
    #if the number of columns of the matrix are diffeent from the number of rows of the vector the multiplication is not to be carried out and the user warned
    if len(matrix[0]) != len(vector):
        print('number of columns of the matrix is different from number of rows of the vector')
    #otherwise the multiplication is performed as usual
    else:
        #create a list for the resultant vector
        res = []
        #traverse the number of rows of the matrix and set a sum variable to 0
        for i in range(0, len(matrix)):
            Sum = 0
            #traverse the length of the vector and add each product between the elements in a row of the matrix and in the vector
            for j in range(0, len(vector)):
                Sum += matrix[i][j] * vector[j]
            #append each sum to the resultant vector
            res.append(Sum)
        return res
#compute the product between matrix D and vector b
c = MatVec(D, b)
print(c)