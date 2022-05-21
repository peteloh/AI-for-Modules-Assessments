# CID: 01720187

# Factorial function

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Sum function

def sum(N):
    if N == 0:
        return 0
    else:
        S = N / fact(N-1) + sum(N-1)
        return S


# Test with Sum to N=15
print(sum(15))
