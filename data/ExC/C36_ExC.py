# Read the file
f = open('CV19.txt','r')
A = f.readlines()
f.close()

print(len(A))

W1 = 0
for i in range(2,15,2):
    W1 = W1 + int(A[i])
W2 = 0
for i in range(17,30,2):
    W2 = W2 + int(A[i])
W3 = 0
for i in range(32,45,2):
    W3 = W3 + int(A[i])
W4 = 0
for i in range(47,60,2):
    W4 = W4 + int(A[i])
W5 = 0
for i in range(62,75,2):
    W5 = W5 + int(A[i])
W6 = 0
for i in range(77,90,2):
    W6 = W6 + int(A[i])
W7 = 0
for i in range(92,105,2):
    W7 = W7 + int(A[i])
W8 = 0
for i in range(107,120,2):
    W8 = W8 + int(A[i])
W9 = 0
for i in range(122,135,2):
    W9 = W9 + int(A[i])
W10 = 0
for i in range(137,150,2):
    W10 = W10 + int(A[i])
W11 = 0
for i in range(152,165,2):
    W11 = W11 + int(A[i])
W12 = 0
for i in range(167,180,2):
    W12 = W12 + int(A[i])
W13 = 0
for i in range(182,195,2):
    W13 = W13 + int(A[i])

# Q1

Sum = W1+W2+W3+W4+W5+W6+W7+W8+W9+W10+W11+W12+W13
print(Sum)

# Q2

print(W1)
print(W2)
print(W3)
print(W4)
print(W5)
print(W6)
print(W7)
print(W8)
print(W9)
print(W10)
print(W11)
print(W12)
print(W13)

# Q3

for i in range(2,15,2):
    if (int(A[i]) > 2000):
        print(A[i-1])
        
for i in range(17,30,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(32,45,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(47,60,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(62,75,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(77,90,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(92,105,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(107,120,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(122,135,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(137,150,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(152,165,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(167,180,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

for i in range(182,195,2):
    if (int(A[i]) > 2000):
        print(A[i-1])

# Q4

I2 = ((W2-W1)/W1)*100
I3 = ((W3-W2)/W2)*100
I4 = ((W4-W3)/W3)*100
I5 = ((W5-W4)/W4)*100
I6 = ((W6-W5)/W5)*100
I7 = ((W7-W6)/W6)*100
I8 = ((W8-W7)/W7)*100
I9 = ((W9-W8)/W8)*100
I10 = ((W10-W9)/W9)*100
I11 = ((W11-W10)/W10)*100
I12 = ((W12-W11)/W11)*100
I13 = ((W13-W12)/W12)*100

print(I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13)

# Q5
List = [W1,W2,W3,W4,W5,W6,W7,W8,W9,W10,W11,W12,W13]
Max = List[0]
for i in range(0,13):
    if List[i] > Max:
        Max = List[i]
print(Max)