# read the file
f = open('CV19.txt','r')
t = f.readlines()
f.close()
Nt = len(t)
N = int(Nt/2)

RN = range(0,N)
#Removed the week tags from the data to make it easier to read can separate in to 7 tuples to determine weeks
CV19 = [] 
c = 0
for i in RN:
    CV19 += [( t[c].rstrip() , int(t[c+1].rstrip()) )]
    c += 2
#1    
S=0
for i in CV19:
    S += i[1]
print('The sum of infections is', S)

#2
p=0
S1=0
for i in CV19:
    
    S1 += i[1]
    p += 1
    if p==7:
        break
print('Week 1 infections are',S1)

p=0
S2=0
for i in CV19:
    
    S2 += i[1]
    p += 1
    if p==14:
        break
print('Week 2 infections are',S2-S1)
#3
f = open('CV19.txt','r')
t = f.readlines()
f.close()
N = len(t)
print(N)