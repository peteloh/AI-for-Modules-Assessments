# Put CID in a list 
CID = [0,1,7,2,1,6,5,1]

# Create Matrix A 
A = []

for i in range(0,8): 
    #Create empty matrix
    A += [[]]
    for j in range(0,8):
        #If on the diagonal, add the correct CID digit for the corresponding row. Else, make the value 0
        if i == j or i + j == 7:
            A[i] += [CID[i]] 
        else:
            A[i] += [0]

# Create Transpose of A

At = [] 

for i in range(0,8):
    #Create empty matrix
    At += [[]]
    for j in range(0,8): 
        
        # Make Aji == Atij, ie swap rows for columns
        At[i] += [A[j][i]] 

# Create B 
B = [] 

# B is a matrix with 8 rows 
for i in range(0,8): 
    # Add the corresponding CID digit to each row of B
    B += [[CID[i]]]
    
# Compute the dot product
C = 0
for i in range(0,8):
    for j in range(0,8):
        C += (A[i][j]-At[i][j])*(B[i][0])
print(C)