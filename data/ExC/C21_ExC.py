#CID no : 01773062

#open and read the txt file
fm = open('CV19.txt','r')
a = fm.readlines()
fm.close()

#i is used to scroll the index of the list a
i = 0
#number of weeks = 13
RW = range(1,14)
for w in RW:
    #week number
    week = a[i].rstrip()
    i+=1
    #date
    #number of days = 7
    Ri = range(1,8)
    for m in Ri :
        date = a[i].rstrip()
        i += 1
        #set the number of infections to 0 first
        infections = 0
        for x in date :
            infections += int(a[i])
print(infections)

#weekly infections 
for w in RW:
    week += [w]
    Sum = 0 # sum of infections = 0
    for date in Ri :
        dates += [date]
        for i in date :
            Sum += int(a[i + week*13].rstrip())
    print(Sum)

