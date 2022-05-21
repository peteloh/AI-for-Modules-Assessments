#CID no: 01773062

CID = [0,1,7,7,3,0,6,2]
#compute Matrix A
A = []
row = []
#range of row of Matrix A
R = range(0,8)
#range of column of Matrix A
C = range(0,8)

for i in R:
    row += [0]

for i in R:
    A += [[]]
    for j in C:
        Rm = range(0,len(CID))
        for k in Rm:
            if i == j or j==len(CID)-1-i :
                A[i] += [CID[i]]
            else :
                A[i] += [0]
            row[j] += A[i][j]

#print(A)

#since my code above does not work, i will write out matrix A and B manually
A = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,7,7,0,0,0],[0,0,0,3,3,0,0,0],[0,0,0,0,0,0,0,0],[0,6,0,0,0,0,6,0],[2,0,0,0,0,0,0,2]]
B = [[0],[2],[3],[4],[5],[6],[7],[8]]

#write a function to compute C
def Mat(A,B):
    # compute range of matrix C
    C = [[0 for x in range(len(B[0]))] for y in range(len(A))]
    # 3 for loops for a multiplication matrix 
    for i in range(0,len(A)):
        for j in range(0,len(B[0])):
            for k in range(0,len(A[0])):
                # C = (A - A transpose) * B
                C[i][j] += (A[i][k]-A[j][k])*B[k][j]
    return C

C = Mat(A,B)
print(C)
