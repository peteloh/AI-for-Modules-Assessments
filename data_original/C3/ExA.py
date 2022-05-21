
def makeArrays(cid):
    A = []
    B = []
    for i, x in enumerate(cid):
        sub = [0]*8
        sub[i] = int(x)
        sub[8-i-1] = int(x)
        A.append(sub)
        B.append(int(x))
    return A, B

def transpose(arr):
    new_arr = []
    for i in range(len(arr)):
        sub = []
        for j in range(len(arr[0])):
            sub.append(arr[j][i])
        new_arr.append(sub)
    return new_arr

def subtract(X, Y):
    arr = []
    assert(len(X) == len(Y))
    assert(len(X[0]) == len(Y[0]))
    for i in range(len(X)):
        sub = []
        for j in range(len(X[0])):
            sub.append(X[i][j] - Y[i][j])
        arr.append(sub)
    return arr

def multiply(A, b):
    c = []
    assert(len(A) == len(b))
    assert(len(A[0]) == len(b))
    for i in range(len(A)):
        acc = 0
        for j in range(len(b)):
            acc += A[i][j] * b[j]
        c.append(acc)
    return c

cid = '01704452'
A, b = makeArrays(cid)
At = transpose(A)
Ax = subtract(A, At)
c = multiply(Ax, b)
print(c)

# Answer: [-4, -20, 12, -16, 0, -21, 4, 0]
    
