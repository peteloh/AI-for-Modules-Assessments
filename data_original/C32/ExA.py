#01702538


def Transpose(A):
    T = []
    #traversing across columns first
    for j in range(0,len(A[0])):
        R = []
        #then traverse down rows
        for i in range(0,len(A)):
            R.append(A[i][j])
        T.append(R)
    return T

def SubtractMatrix(A,B):
    #check if matrices can be subtracted
    if (len(A),len(A[0])) != (len(B),len(B[0])):
        return 'Matrices not compatible.'
    else:
        C = []
        #traverse down rows
        for i in range(0,len(A)):
            R = []
            #traverse across columns
            for j in range(0,len(B)):
                #Subtract terms
                R.append(A[i][j]-B[i][j])
            C.append(R)
    return C

def MatArr(A,B):
    #check if they can be multipled
    if len(A[0]) != len(B):
        return 'Matrix and array are not compatible.'
    else:
        C = []
        #traverse down rows of A
        for i in range(0,len(A)):
            R = []
            #sum each row*column
            S = 0
            #will only append through 1 value of j
            for j in range(0,len(A[0])):
                S += A[i][j]*B[j]
            R.append(S)
            C.append(R)
        return C

def A(CID):
    #size of matrix
    N = 8
    A = []
    for i in range(0,N):
        R = []
        for j in range(0,N):
            #Only append value if on the diagonal
            if j == i or j == N-1-i:
                R.append(CID[i])
            else:
                R.append(0)
        A.append(R)
    return(A)

 
    
CID = [0,1,7,0,2,5,3,8]

A = A(CID)
#Transpose A
AT = Transpose(A)
B = CID

C = MatArr(SubtractMatrix(A,AT),B)

#for i in range(0,len(A)):
#    print(A[i])
#
#for i in range(0,len(AT)):
#    print(AT[i])
#    
#for i in range(0,len(C)):
#    print(C[i])

    
    
    
    
    
    
    
    
    