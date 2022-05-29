#Task A:
#Process:
#need to create a function that creates the matrix pattern upon a user input
#the user inputs the size of the matrix
#then create a function that computes the c=(AAT).b matrix 

#Create the 8 x 8 matrix A
A = [ [0,0,0,0,0,0,0,0] , [0,1,0,0,0,0,1,0] , [0,0,7,0,0,7,0,0] , [0,0,0,0,0,0,0,0], [0,0,0,4,4,0,0,0], [0,0,9,0,0,9,0,0], [0,9,0,0,0,0,9,0], [5,0,0,0,0,0,0,5]]
for row in A:
    print(row)

#Create the matrix B

b = [[0],[1],[7],[0],[4],[9],[9],[5]]
N = int(input('N:  '))
RN = range(0,N)
A = [] # initialise the matrix as a list
for i in RN:
    # form i-th row
    row = [] # initialise i-th row as a list
    for j in RN:
        # add j-th column into i-th row
        if j == i or j == N-i-1:
            row += [1]
        else:
            row += [0]
    # add row i-th to the matrix A
    A += [row]

for row in A:
    print(row) 
    
#to form the Transpose of A, A^T