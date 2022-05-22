f=open('CV19.txt','r')
t=f.readlines()
f.close()
print(t)

N= len(t)
RN=range(0,N)
week = [] # list of weeks
c = 0
for i in RN:
    week += [( t[c].rstrip() , (t[c+1].rstrip()) ,int(t[c+2].rstrip()) )]
    c += 3
#1    
S = 0
for i in RN:
    S += week[i][2]
print(S)

#2
for i in RN:
    Rj = range(i+1,N)
    for j in Rj:
        for k in range(j+1,N):
            

#3
for i in RN:
    Rj = range(i+1,N)
    for j in Rj:
        for k in range(j+1,N):
            found=False
            if week[i][2]>2000:
                count+=count +1
            else:
                c+= +3

#4
I=[]
y= 100*(week[i][1]-week[i-1][1])/week[i-1][1]
for i in RN:
    Rj = range(i+1,N)
    for j in Rj:
        y+= j




#5
for i in RN:
    Rj = range(i+1,N)
    for j in Rj:
        for k in range(j+1,N):
            if week[i][2] < week[j][2]:
            # swap these two weeks
            (week[i], week[j]) = (week[j], week[i])
            weekMax= week[N+1]            #last week
for item in week:
    print(item)  

    