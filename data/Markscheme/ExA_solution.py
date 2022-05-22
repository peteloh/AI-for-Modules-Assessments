# enter CID
CID = '01302327'


b = []
for i in range(0,8):
    b += [int(CID[i])]
print('CID')

# Ex 1    
N = len(b)

# set matrix A
A = []
for i in range(0,N):
    # set this row
    row = []
    for j in range(0,N):
        # select diagonal or anti-diagonal
        if i==j or j==N-i-1:
            # diagonal or anti-diagonal: write digit from my CID
            el = b[i]
        else:
            # outside digonals: write 0
            el = 0
        row += [el]
    A += [row]

# solve in one iteration
# determine c
c = []
for i in range(0,N):

    # initialise sum
    s = 0
    for j in range(0,N):
        s += (A[i][j]-A[j][i])*b[j]
    c += [s]

print('c')
print(c)


print()
print('A')
for row in A:
    print(row)

####################################################### solve step by step
# determine AT
AT = []
for i in range(0,N):
    # set this row
    row = []
    for j in range(0,N):
        row += [A[j][i]]
    AT += [row]
    
print('At')     
for row in AT:
    print(row)
    
        
# A- At
D = []
for i in range(0,N):
    # set this row
    row = []
    for j in range(0,N):
        row += [A[i][j]-AT[i][j]]
    D += [row]
    
print('A-At')   
for row in D:
    print(row)

# determine c
c = []
for i in range(0,N):
    # set this row
    # initialise sum
    s = 0
    for j in range(0,N):
        s += D[i][j]*b[j]
    c += [s]

#print('c')
#print(c) 