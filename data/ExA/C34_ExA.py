# -*- coding: utf-8 -*-
"""
Question 1 Computing Exam


"""

def printMatrix (matrix): #prints matrix in cleaner format
    for row in matrix:
        print (row)

def MatrixSubtraction (matrix1, matrix2):
    #determines dimensions of both matrices
    rowsmatrix1 = len(matrix1)
    columnsmatrix1 = len(matrix1[0])
    rowsmatrix2 = len(matrix2)
    columnsmatrix2 = len(matrix2[0])
    #creates two empty lists that act as output row and output matrix
    outputmatrix = [] 
    outputrow = []
    #check dimensions to make sure they can be subtracted
    if rowsmatrix1 != rowsmatrix2 or columnsmatrix1 != columnsmatrix2:
        return 'cannot add matrices of different dimensions'
    else:
        for i in range (rowsmatrix1): #iterates through rows
            for j in range (columnsmatrix1): #iterates through columns
                outputrow.append((matrix1[i][j])-matrix2[i][j]) #subtracts element in the same positions and appends to the output row list
        for k in range (rowsmatrix1):
            outputmatrix.append(outputrow[k*columnsmatrix1:(k+1)*columnsmatrix1]) #the output row list is split into smaller lists depending on the dimensions of the input matricies to form the output matrix
    return outputmatrix #output matrix outputted

def Transpose (matrix):
    transposedmatrix = [] # Creates an empty list that matrix rows can be inputted into
    newrow = [] # Creates an empty list that transposed values will be added into. This wholes list will then be inserted into the transposed matrix
    num_rows_matrix = len(matrix) # Calculates and stores the number of rows of the inputted matrix
    num_columns_matrix = len(matrix[0]) # Calculates and stores the number of columns of the inputted matrix
    for i in range (num_columns_matrix): # Iterates through the ith row the matrix
        for j in range (num_rows_matrix): # Iterates through jth column in the ith row of the matrix
            newrow.append(matrix[j][i]) # Finds the value with the row value of j and the columns value of i and appends it to the new row list
        transposedmatrix.append(newrow) # This newrow is then appended into the transposed matrix
        newrow = [] # The new row is cleared for the next iteration
    # this is repeated for all columns rows in the matrix 
    return transposedmatrix # The transposed matrix is outputted

A = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,0,0,0,0,0],[0,0,0,5,5,0,0,0],[0,0,4,0,0,4,0,0],[0,9,0,0,0,0,9,0],[3,0,0,0,0,0,0,3]] #matrix made up of my CID
At = Transpose(A)
A_minus_At = MatrixSubtraction (A, At)
B = [[0],[1],[7],[0],[5],[4],[9],[3]] #matrix B made up of my CID

#def DotProduct (Matrix,Vector):
#    rowsMatrix = len(Matrix)
#    columnsMatrix = len(Matrix[0])
#    rowsVector = len(Vector)
#    if rowsMatrix != rowsVector:
#        return 'error'
#    count = 0
#    for i in range (rowsMatrix):
#        for j in range (columnsMatrix):
#            print((Matrix[i][j]*Vector[j]))
#    return count

def MatrixMultiply (matrix1,matrix2):
    product = [] #creates an empty list where the output matrix will be appended into
    c = 0 #a temporary variable where the sum of the elements of matrix 1 and matrix 2 will be stored
    number_of_rows_of_matrix1 = len(matrix1) #stores the number of rows in matrix 1
    number_of_columns_of_matrix1 = len(matrix1[0]) #stores the number of columns in matrix 1
    number_of_rows_of_matrix2 = len(matrix2) #stores the number of rows in matrix 2
    number_of_columns_of_matrix2 = len(matrix2[0]) # stores the number of columns in matrix 2
    if number_of_columns_of_matrix1 != number_of_rows_of_matrix2:
        print ('0') #checks whether the two matrices can be multiplied. If they cant, 0 is returned
    else:
        for i in range (number_of_rows_of_matrix1): #selects the correct row of matrix 1
            #product.append(templist)
            templist = [] # creates a temporary list
            for k in range (number_of_columns_of_matrix2): #selects the correct column of matrix 2
                for j in range (number_of_columns_of_matrix1): # selects the correct column of matrix 1
                    c += (float(matrix1[i][j]) * float(matrix2[j][k])) # adds the product of the element in the ith row and jth column and the element in the jth row and kth column to c
                templist.append(c) #After all the columns in matrix 1 exhausted, the sum,c, is appended to the temporary list
                c=0 #c is cleared before the next iteration
                if k == int(number_of_columns_of_matrix2-1): 
                    product.append(templist) #when the last matrix column of matrix 2 is reached, append the temporary list (the row of the product matrix) to the product list   
        return product #return the product of the matrix
    
c = MatrixMultiply (A_minus_At,B) #Matrix multiplication. 
print (c) #returns answer