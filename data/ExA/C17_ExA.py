# CID: 01710404

A = [[0,0,0,0,0,0,0,0],   #making matrix A
     [0,1,0,0,0,0,1,0],
     [0,0,7,0,0,7,0,0],
     [0,0,0,1,1,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,4,0,0,4,0,0],
     [0,0,0,0,0,0,0,0],
     [4,0,0,0,0,0,0,4]]

def Transpose(A):            #making function to transpose
    a = len(A)   #rows
    b = len(A[0])    #columns
    
    T = []   #need empty matrix to fill
    
    for i in range(0,a):
        row = []  #traversing rows and adding empty tuple
        for j in range(0,b):
            row += [A[j][i]]  #traversing rows and columns and swapping the row index with column index
        T += [row]  #adding rows to T
    
    return T

AT = Transpose(A)  #getting transpose of A

C = []

for i in range(0,len(A)):
    row = []
    for j in range(0,len(A[0])):
        row += [A[i][j]-AT[i][j]]   #same as before but subtracting AT from A to get C
    C += [row]
        

B = [[0],
     [1],
     [7],     #making B
     [1],
     [0],
     [4],
     [0],
     [4]]

D = []

for i in range(0,len(A)):
    Sum = 0     #making initial value = 0
    for j in range(0,len(B[0])):
        Sum += C[i][j] * B[j]   #adding all of the elements in the j index of B to the same i index of C to get matrix multiplication
    D += [Sum]


for rows in D:
    print(rows)