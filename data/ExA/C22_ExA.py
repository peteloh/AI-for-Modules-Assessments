#CID:01701263

#TaskA
b=[0,1,7,0,1,2,6,3] #CID number

N=8 #8*8 matrix
A=[]
for i in range(0,N):
    row=[]
    for j in range(0,N):
        if i+j==7 or i==j:
            row+=[b[i]]
        else:
            row+=[0]
    A+=[row]
#for i in A:
    #print(i)

def Transpose(A):
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
At=Transpose(A)
#print('')
#for i in At:
    #print(i)

#d=A-At

d=[]
for i in range(0,N):
    row=[]
    for j in range(0,N):
        row+=[A[i][j]-At[i][j]]
    d+=[row]
#print('')
#for i in d:
    #print(i)
    
def MatVec(A,b):
    # this function computes the matrix vector multiplication between A and b
    # c = A . b    

    # check if dimensions are compatible
    N = len(A) # number of rows
    M = len(A[0]) # number of columns
    # number of columns of A must equal the length of b
    if M == len(b):
        # dimensions are compatible: do the multiplication
        c = []
        RN = range(0,N)
        RM = range(0,M)
        for i in RN:
            # compute c(i)
            sum = 0
            for j in RM:
                sum += A[i][j] * b[j]
            c += [sum]
    else:
        # dimensions are not compatible, return the value of zero
        c = 0
        
    return c
c=MatVec(d,b)
print(c)

