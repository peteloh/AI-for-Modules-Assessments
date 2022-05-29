# read the file
f = open('CV19.txt','r')
b = f.readlines()
f.close()


# repeat for every week
Rw = range(0,12)
Data = []
i = 0
for m in Rw: 
    # register this month
    week = str(b[i].rstrip())
    i += 15
    # register num of days
    N = 14
    RN = range(1,N)
    Day = []
    j = 0
    for n in RN:
        Day += [(b[m*14+n +j].rstrip(),b[m*14 +n + j +1].rstrip())]
        j +=1
    Data += [(week,Day)]

for week in Data:    
    print (week)
    print ()

