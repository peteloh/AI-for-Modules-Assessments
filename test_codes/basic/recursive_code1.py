def Sum(N):
    if N == 2:
        S = 1
    else:
        S = 3**(N-2) + Sum(N-1)
    return S

#
a = Sum(5)
print(a)