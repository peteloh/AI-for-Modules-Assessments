#c= (A-At).b

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


def minusmatrices(A,B):   #c=A-B
    n1 =range(0,len(A))              # N1rows
    m1 =range(0,len(A[0]))                # N1columns
    n2 =range(0,len(B))              # N2rows
    m2 =range(0,len(B[0]))           # N2columns
    if n1==n2 and m1==m2:
        result=[]
        for i in n1:
          row =[]
          for j in m2:
              sum =0
              sum += A[i][j]- B[i][j]
              row += [sum]
          result+=[row]            
    else:
        result=0
    return result

def Matmultiply(A,b):
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
        RP=range (0,len(b[0]))
        for i in RM:
        # forming row i
            row = []
            for j in RP:
            # forming C(i,j)
                S = 0
                for k in RM:
                    S += A[i][k]*b[k][j]
                row += [S]
            c += [row]

    else:
        # dimensions are not compatible, return the value of zero
        c = 0
        
    return c


b=[[0],[1],[4],[9],[5],[0],[8],[9]]
A=[[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,4,0,0,4,0,0],[0,0,0,9,9,0,0,0],[0,0,0,5,5,0,0,0],[0,0,0,0,0,0,0,0],[0,8,0,0,0,0,8,0],[9,0,0,0,0,0,0,9]]
At = Transpose(A)
print(At)
M = minusmatrices(A,At)
print(M)
final = Matmultiply(M,b)
print(final)