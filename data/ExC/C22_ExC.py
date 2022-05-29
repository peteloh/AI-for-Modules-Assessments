#CID:01701263

#TaskC
#TaskC
import math as mt
import matplotlib.pyplot as pl

f = open('CV19.txt','r')
b = f.readlines()
f.close()
   
# process the lines and compose the list of tuples
stat = []
# i is used to scroll the index of the list b
i = 0
Day=[]
# repeat for every week
Rm = range(1,14)
for m in Rm:
    # register this week
    week = (b[i].rstrip())
    i += 1
    Day+=[b[i].rstrip()]
    i += 1
    N1=int(b[i])
    i += 1
    Day+=[b[i].rstrip()]
    i += 1
    N2=int(b[i])
    i+=1
    Day+=[b[i].rstrip()]
    i += 1
    N3=int(b[i])
    i += 1
    Day+=[b[i].rstrip()]
    i += 1
    N4=int(b[i])
    i += 1
    Day+=[b[i].rstrip()]
    i += 1
    N5=int(b[i])
    i += 1
    Day+=[b[i].rstrip()]
    i += 1
    N6=int(b[i])
    i += 1
    Day+=[b[i].rstrip()]
    i += 1
    N7=int(b[i])
    i += 1
    stat += [(week,N1,N2,N3,N4,N5,N6,N7)]
for i in stat:
    print(i)

spw=[] #Sum of no. of ppl getting infected every week 
for i in range(0,13):
    s=0
    for j in range(1,8):
        s+=stat[i][j]
    spw+=[s]
print('')
print('Total number of ppl infected per week:')
print(spw)

T=0 #initialise sum=0
for i in spw:
    T+=i
print('')
print('Total number of ppl infected:')
print(T) #Total number of ppl getting infected

incre=[]
for i in range(1,13):
    incre+=[(spw[i]-spw[i-1])/spw[i-1]*100]
print('')
print('Weekly percentage increment:')
print(incre)

week=0
Imax=spw[0]
for i in range(0,13):
    if spw[i]>Imax:
        Imax=spw[i]
        week=i
print('')
print('Highest infection: '+str(Imax)+' at week '+str(week))

D=[] #Sum of no. of ppl getting infected every week 
#print(Day)
print('')
for i in range(0,13):
    for j in range(1,8):
        if stat[i][j]>2000: #if greater than 2000
            D+=[Day[i+j*7]]
print(D)