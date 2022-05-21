#CID:01730549
M=8
N=8
A=[] #initialise matrix
#create 8x8 matrix of zeroes
for i in range(0,M):
    d=[]
    for j in range(0,N):
        d=d+[0]
    A=A+[d]
#change diagonals for CID
A[1][1]=A[1][6]=1
A[2][2]=A[2][5]=7
A[3][3]=A[3][4]=3
A[4][4]=A[4][3]=0
A[5][5]=A[5][2]=5
A[6][6]=A[6][1]=4
A[7][7]=A[7][0]=9
#create 8x1 matrix
b=[[0],[1],[7],[3],[0],[5],[4],[9]]
#D=A-AT
D=[]
for i in range(0,M):
    d=[]
    for j in range(0,N):
        d=d+[A[i][j]-A[j][i]]
    D=D+[d]
c=[]
for i in range(0,M):
    d=[]
    for j in range(0,1):
        sum=0
        for k in range(0,N):
            sum=sum+D[i][k]*b[k][j]
        d=d+[sum]
    c=c+[d]
for i in c:
    print(i)
        
        
        

        