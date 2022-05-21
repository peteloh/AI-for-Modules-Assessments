#CID:01711943
def Transpose(A):
# find size of A
    M = len(A) # number of rows
    N = len(A[0]) # number of columns
    RM = range(0,M)
    RN = range(0,N)
    T = []
    row=[]
    for i in RN:
        row = []
        for j in RM:
            row += [A[j][i]]
        T += [row]
    return T
A=[[0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,1,0],
[0,0,7,0,0,7,0,0],
[0,0,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
[0,0,9,0,0,9,0,0],
[0,4,0,0,0,0,4,0],
[3,0,0,0,0,0,0,3]]
b=[0,1,7,1,1,9,4,3]

#find the transpose of the matrix A
At=Transpose(A)
print(At)
#subtract At from A
S=[]#A-At
for i in range(0,len(A)):
    for j in range(0,len(A[0])):
        S+=[A[i][j]+At[i][j]]

#matrix multiplication of S and b
multrow=[]#row of matrix being multiplied
c=[]#resultant list
element=0#individual element of matrix
row=[]
for i in range(0,len(S)):
    multrow=[S[i]]
    row=[]
    for j in range(0,len(S)):
        element=0
        for k in range(0,len(S)):
            element+=multrow[k]*b[k]
        row+=[element]
    c+=[row]
print(c)
        