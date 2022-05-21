#01779587

#read all the lines of the file 
f = open('CV19.txt','r')
b = f.readlines()
f.close()
N = 13
RN = range(0,N)

#extract data 
RW = range(0,13)
RD = range(0,7)

weeks = []
overall = []
#traverse al data, sequentially and subdivide them in weekly batches
c = 0 
for day in RW: 
    #examine one week 
    weeks += [weeks]
    Sum = 0 #initialise 
    for count in RD: 
        #extract single day 
        CV = int(f[c].rstrip())
        #add this number to overall
        Sum += CV 
print (Sum) #calaculate overall infections in given period 


weekly = []


# days number > 2000
for day in RD: 
    count = 0 
    date = []
    for i in range(0, len(days)):
        if number > 2000: 
            count = count + 1
            date = date + [CV[i][0]]
for item in date: 
    print('date' + str(item[0]))
    
    
    
#week with highest infections 
def SortAscending(RW):
    # this function sorts the values of x
    # Note that the output is the same list, as the input list, but sorted
    Nx = len(RW)
    Ri = range(0,RW)
    #  I am reusing the sorting algorithm we used in Session 5 Task B, with minor modifications
    for i in Ri:
        Rright = range(i+1,RW)
        for j in Rright:
            if x[j] < x[i]:
                # swap 
                (x[j],x[i]) = (x[i],x[j])
    print(x[0])
                

