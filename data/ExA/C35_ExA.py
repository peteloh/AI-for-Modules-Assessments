#CID:01713254
A=[]
#create an empty list to represent matrix A
CID=[0,1,7,1,3,2,5,4]
#create a list, consisting of my CID number
for i in range(0,8):
    row=[]
    for j in range(0,8):
        if i==j or i==7-j:
            row+=[CID[i]]
        else:
            row+=[0]
            #0 elsewhere
    A+=[row]
#Now create A Transpose
AT=[]
for i in range(0,8):
    row=[]
    for j in range(0,8):
        row+=[A[j][i]]
    AT+=[row]
#Compute A-AT:
AAT=[]
for i in range(0,8):
    row=[]
    for j in range(0,8):
        row+=[A[i][j]-AT[i][j]]
    AAT+=[row]
#Compute the product
b=[0,1,7,1,3,2,5,4]
AATb=[]
#This is the product of AAT with b
for i in range(0,8):
    Sum=0
    for j in range(0,8):
        Sum+=AAT[i][j]*b[j]
    AATb+=[Sum]

    
