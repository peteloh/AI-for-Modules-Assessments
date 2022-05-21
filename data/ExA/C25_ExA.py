# CID: 01720187

# N = size of matrix A
Na = 8

# A is 8x8 blank matrix
A = [[0 for row in range(Na)] for col in range(Na)]

b = [0, 1, 7, 2, 0, 1, 8, 7]

# Replace values in A with CID
for i in range(Na):
    for j in range(Na):
        if i == j or Na-i-1 == j:
            A[i][j] = b[i]

# Transpose A to T
T = [[A[j][i] for j in range(Na)] for i in range(Na)]

# AAT is A-T
AAT = []

# Subtract T from A
for i in range(Na):
    row = []
    for j in range(Na):
        row += [A[i][j] - T[i][j]]
    AAT += [row]

# c = AAT . b

# C - blank matrix
C = [0 for col in range(Na)]
print(C)

# Dot product
for i in range(Na):
        for j in range(Na):
            C[i] = A[i][j] * b[j]

print(AAT)
print(C)