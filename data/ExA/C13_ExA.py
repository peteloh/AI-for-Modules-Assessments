#My CID number is 01700084

B = [[0],[1],[7],[0],[0],[0],[8],[4]]

N = 8
R = range(0,N)
A =[]


for i in R:
    Row =[]
    for j in R:
        if j==i or j == N - i -1:
            Row = Row + [B[i][0]]
        else:
            Row = Row + [0]
    A = A + [Row]

def Transpose(A): #defining function to create Transpose of A
    # find size of A
    M = len(A) # number of rows
    N = len(A[0]) # number of column
    RM = range(0,M)
    RN = range(0,N)
    T = []
    for i in RN:
        row = []
        for j in RM:
            row += [A[j][i]]
        T += [row]
    return T
            
AT = Transpose(A) #This is transpose of A

def dot(v1, v2):
     return sum(x*y for x,y in zip(v1,v2))

D = [] #to create matrix of A - AT

for i in R:
    Row = []
    for j in R:
        Row = Row + [A[i][j]-AT[i][j]]
    D = D + [Row]

C = dot(A, B)

print(C)
