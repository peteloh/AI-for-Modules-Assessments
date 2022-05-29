# Set CID number as a string
CID = '01759109'

# Open Matrix A
A = []
# Set all indices as zero
for i in range(0,8):
    Row = [] #set the rows
    for j in range(0,8):
        Row = Row + [0] #add columns into rows
    A = A + [Row]

# Change indices in both diagonals into CID numbers
for i in range(0,8):
    A[i][i] = CID[i]
    A[i][7-i] = CID[i]
    
for R in A:
    print(R)