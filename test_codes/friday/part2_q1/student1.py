"""
100% correct code
""" 

def Decompose(A):
    N = len(A)
    RN = range(0,N)   
    T = []
    for i in RN:
        row = []
        for j in RN:
            Sum = 0
            for k in RN:
                c = 0
                d = 0
                e = 0
                if k == j:
                    d = A[k][j]
                if i > k: 
                    c = A[i][k]
                if i < k:
                    e = A[i][k]
                Sum += c*d+e*d
            row += [Sum]
        T += [row]
    return T