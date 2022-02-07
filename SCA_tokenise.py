import io
import tokenize

code1 = b"""
x = 0
while x<=10: # should run 10 times
    x+=1
"""

code2 = b"""
for i in range(0,5):
    continue
"""

code3 = b"""
def Decompose(A):
    N = len(A)
    RN = range(0,N)   
    # NO NEED to compute firstly the three matrices C, D, E
    # compute T directly
    T = []
    for i in RN:
        row = []
        for j in RN:
            Sum = 0
            for k in RN:
                # if we had the matrices C, D and E we would have done
                #Sum += C[i][k]*D[k][j]+E[i][k]*D[k][j]
                # however the values of C[i][k], D[k][j] and E[i][k] would be zero ....
                c = 0
                d = 0
                e = 0
                # ... unless:
                if k == j: # we are on the diagonal for D
                    d = A[k][j]
                if i > k: # we are in the lower triangle for C
                    c = A[i][k]
                if i < k: # we are in the upper triangle for E
                    e = A[i][k]
                # in which cases: they would be the value in the corresponding position of A
                
                Sum += c*d+e*d
            row += [Sum]
        T += [row]
    return T

#
A = [[1,2,3,4,5,6],[6,0,3,4,2,1],[2,1,9,4,6,7],[3,0,8,4,6,5],[1,5,4,3,3,1],[6,1,4,4,3,2]]
for row in A:
    print(row)
print()
T = Decompose(A)
print()
for row in T:
    print(row)
"""

for token in tokenize.tokenize(io.BytesIO(code3).readline):
    print(token)