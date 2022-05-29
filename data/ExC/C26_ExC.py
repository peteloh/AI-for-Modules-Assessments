#CID:01730549
#1
def ReadFileStr(A):
    a=f.readlines()
    astrip=[]
    for i in a:
        astrip=astrip+[i.rstrip()] #removes \n in each line
    f.close()
    return(astrip)
f=open('CV19.txt','r')
f1=ReadFileStr(f)
#each 15 term is a week
#date going from odd to even and back to odd every week change
#number of infection going from even to odd and back to even every week change
#need to simplify the file
f2=[]
i=0
while(i<len(f1)):
    if i%15==0: #get rid of weeks in the file
        i=i+1
    f2=f2+[f1[i]]
    i=i+1
sum=0
for i in range(0,len(f2)):
    if i%2!=0:
        sum=sum+int(f2[i])
print('overall number of infections=',sum)

#2
avg=sum/13 #13 total weeks
print('weekly average=',avg)

#3
l=[] #initiate list
for i in range(0,len(f2)):
    if i%2!=0 and int(f2[i])>2000:
        l=l+[str(f2[i-1])]
print('list of days when number of infections>2000:')
for i in l:
    print(i)

#4
w=[]
w=w+[3+12+38+29+49+43+67]#1st week
s=0
for i in range(1,len(f2)):
    
    if i%2!=0:
        s=s+int(f2[i])
    if i%14==0:
        w=w+[s]
        s=0
    w=w+[s]
        
        
print(w)

#5
max=0
for i in range(0,len(w)):
        if(int(f2[i])>max):
            max=int(f2[i])
    




        
    


    