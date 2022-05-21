#TaskA my CID is 01742057
MatA = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,7,0,0,7,0,0],[0,0,0,4,4,0,0,0],[0,0,0,2,2,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,5,0],[7,0,0,0,0,0,0,7]]
MatB = [0,1,7,4,2,0,5,7]
# now transpose the matrix A
AT = []
for i in range(0,8):
    row = []
    for k in range(0,8):
        row.append(MatA[k][i])
    AT.append(row)
print(MatA)
print(AT)

#now do A-A^T
bracketpart = []
for i in range(0,8):
    row1 = []
    for k in range(0,8):
        row1.append(MatA[i][k]-AT[i][k])
    bracketpart.append(row1)
print(bracketpart)

#now multiply matrix
CMasterlist = []
for j in range(0,8):
    for k in range(0,8):
        Crow = []
        for i in range(0,8):
            aii = 0
            aii = aii + (bracketpart[k][i]*MatB[i])
        Crow.append(aii)
    CMasterlist.append(Crow)
    
print(CMasterlist)