#01703867
f=open('CV19.txt','r') # open file and read it line by line
a=f.readlines()
f.close() # close file
Infections=[] # initialise list
i=0
Rw=range(1,14) # 13 weeks therefore range is (1,14)
for w in Rw:
    week=a[i]
    i+=1
    date=a[i]
print(week,date)
#did not complete