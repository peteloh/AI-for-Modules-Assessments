#Function to carry out maths
def array(A,AT,b):
    for i in range(0,N):
        c = (A[i]-AT[i])*b[i]
    return c

#In main script form Matrix A, AT, b   
#For A (attempt 1)
N = input('Size of Matrix A = ')
N = int(N)
A = []
for m in range(0, N):
    matrix = []
    for n in range(0,N):
        if n == m ==0:
            matrix += [0]
        if n == m ==1:
            matrix += [1]
        if n == m ==2:
            matrix += [7]
        if n == m ==3:
            matrix += [1]
        if n == m ==4:
            matrix += [3]
        if n == m ==5:
            matrix += [9]
        if n == m ==6:
            matrix += [5]
        if n == m ==7:
            matrix += [6]
        else:
            matrix += [0]
    A += [matrix]
print('Matrix A is')
for matrix in A:
    print(matrix) 

#For A (attempt 2)
A = [[0,0,0,0,0,0,0,6],[0,1,0,0,0,0,0,0],[0,0,7,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,3,0,0,0],[0,0,0,0,0,9,0,0],[0,0,0,0,0,0,5,0],[0,0,0,0,0,0,0,6]]
print('Matrix A is')
for y in A:
    print(y)

#For AT
AT = [[0,0,0,0,0,0,0,6],[0,0,0,0,0,0,5,0],[0,0,0,0,0,9,0,0],[0,0,0,0,3,0,0,0],[0,0,0,1,0,0,0,0],[0,0,7,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
print('Matrix AT is')
for x in AT:
    print(x)

#For b
b = [[0],[1],[7],[1],[3],[9],[5],[6]]
print('Matrix b is')
for r in b:
    print(r)

#Call the function array to carry out the maths
array(A,AT,b)