#CID = 01712921


A = [(0,0,0,0,0,0,0,0),(0,1,0,0,0,0,1,0),(0,0,7,0,0,7,0,0),(0,0,0,1,1,0,0,0),(0,0,0,2,2,0,0,0),(0,0,9,0,0,9,0,0),(0,2,0,0,0,0,2,0),(1,0,0,0,0,0,0,1)]
b = [(0),(1),(7),(1),(2),(9),(2),(1)]


#Find transpose of A
def Transpose(A):
    # find size of A
    # find the number of rows
    M = len(A) 
    # find the number of columns
    N = len(A[0]) 
    RM = range(0,M)
    RN = range(0,N)
    #set up T
    T = []
    #go through matrix and transpose
    for i in RN:
        row = []
        for j in RM:
            row += [A[j][i]]
        T += [row]
    return T

q = Transpose(A)


#Find A minus transpose of A
# set up sub
sub = [] 
N = len(A[0])
RN = range(0,N)
for i in RN:
    # compute row i
    # set up row i
    row = [] 
    for j in RN:
        # compute column j in row i 
        row += [A[i][j] - q[i][j]]
    # add row i to matrix sub
    sub += [row]



#Muliply with matrix b    
def Matmulti(A,B):
    # this function computes the matrix vector multiplication between two matrixes
    # number of rows     
    N = len(A) 
    # number of columns
    M = len(A[0]) 
    c = []
    RN = range(0,N)
    RM = range(0,M)
    for i in RN:
        # compute c(i)
        sum = 0
        for j in RM:
            sum += A[i][j] * B[i]
        c += [sum]
        
    return c

c = Matmulti(sub,b)
print(c)




























