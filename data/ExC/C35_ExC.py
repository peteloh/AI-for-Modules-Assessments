#CID:01713254
f=open('CV19.txt ','r')
c=f.readlines()
C=[]
for i in range(0,len(c)-1):
    C+=[c[i].rstrip()]
M=len(C)
N=int(M/15)
#N is the number of weeks
#print(C)
print(M,N)
#Now find the overall number of infections
#Organize the list into a list of tuples
Co=[]
for i in range(0,M,15):
    week=(C[i],C[i+1],C[i+2],C[i+3],C[i+4],C[i+5],C[i+6],C[i+7],C[i+8],C[i+9],C[i+10],C[i+11],C[i+12],C[i+13],C[i+14])
    Co+=[week]
for row in Co:
    print(row)
n=0
#n: total number of infection
#print(type(int(Co[0][4])))
for i in range(0,len(Co)):
    for j in range(2,15,2):
        n+=int(Co[i][j])
print(n)
nweek=[]
#number of infection per week
for i in range(0,len(Co)):
    inweek=0
    #number of infection at week i+1
    for j in range(2,15,2):
        inweek+=int(Co[i][j])
    nweek+=[inweek]
print(nweek)
    