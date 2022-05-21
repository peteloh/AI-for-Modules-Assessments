#01703867
def Transpose(A): # function to find transpose of A
    N=len(A)
    RN=range(0,N)
    AT=[]
    for i in RN:
        row=[]
        for j in RN:
            row+=[A[j][i]]
        AT+=[row]
    return AT
def Multiply(S,B): # function to multiply matrices S and b
    M=len(S) # rows of S
    MS=len(S[0]) # columns of S
    P=len(B[0]) # rows of B
    RM=range(0,M) # define ranges
    RN=range(0,MS)
    RP=range(0,P)
    C=[] # compjute product of S and b
    for i in RM:
        row=[] # compute row i of matrix
        for j in RP: # compute column
            Sum=0 # initalise
            for k in RN:
                Sum+=S[i][k]*B[k][j]
            row+=[Sum] # append this column
        C+=[row] # append this row
    return C
# make matrix A
A=[[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,0,0,0,0,0],[0,0,0,3,3,0,0,0],[0,0,8,0,0,8,0,0,],[0,6,0,0,0,0,6,0],[7,0,0,0,0,0,0,7]]
AT=Transpose(A) # Transpose computed using function
S=[] # S=A-AT
N=len(A)
RN=range(0,N)
for i in RN: # compute row of matrix from subtraction
    row=[]
    for j in RN:# compute column of matrix from subtraction
        row+=[A[i][j]-AT[i][j]]
    S+=[row] # append columns
b=[[0],[1],[7],[0],[3],[8],[6],[7]] # make array b
c=Multiply(S,b) # use multiply function to find c
for row in c:
    print(row) # print answer