"""
whole 3rd nested loop mising - logic extremely wrong
""" 

def Decompose(A):
    N = len(A)
    RN = range(0,N)   
    T = []
    for i in RN:
        row = []
        for j in RN:
            Sum = 0
            c = 0
            d = 0
            e = 0
            if k == j:
                d = A[1][j]
            if i > k: 
                c = A[i][1]
            if i < k:
                e = A[i][1]
            Sum += c*d+e*d
            row += [Sum]
        T += [row]
    return T