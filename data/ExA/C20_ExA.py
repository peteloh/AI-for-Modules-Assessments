#01718219

CID = [0,1,7,1,8,2,1,9]

#produce vector B
B = []
for i in range(0,len(CID)):
    row = []
    row = row + [CID[i]]
    B = B + [row]
        
for row in B:
    print(row)


#produce matrix A
A = []
for i in range(0,len(CID)):
    row = []
    for j in range(0,len(CID)):
        if i == j or j == N-1-i:
            row = row + [CID[i]]
        else:
            row = row + [0]
    A = A + [row]
for row in A:
    print(row)
    

#subtraction of matrices:
Z = []
for i in range(0,len(A)):
    row = []
    for j in range(0,len(A[0])):
        #row and column swapped for transpose
        row = row + [A[i][j] - A[j][i]]
    Z = Z + [row]

for row in Z:
    print(row)
    
#dot product
sum = 0
for i in range(0,len(Z)):
    for j in range(0,len(B)):
        sum = sum + Z[i][j]*B[j][0]

#test
print(sum)
