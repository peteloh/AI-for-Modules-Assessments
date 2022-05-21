#CID:01711943
#open the file
f = open('CV19.txt','r')
t = f.readlines()
f.close()
# extract the data of weeks, dates and infections
data = []
for item in t:
    data += [(item.rstrip())]
    

#list of weeks with tuple of day number and infection number
#to find number of infections in given period
organised=[]#organised data with week number eliminated for easier analysis
for i in range(0,len(data)-1):
    if i%15!=0:
        organised+=[data[i]]
#convert number of cases to int
for i in range(0,len(organised)):
    if i%2==1:
        organised[i]=int(organised[i])
#print(organised)        
#to find overall number of infections  
totalInf=0
for i in range(1,len(organised),2):
    totalInf+=organised[i]
print('total infections:'+str(totalInf))

#weekly number of infections 
weeklyData=[]#organised per week
start=0
week=[]
for i in range(0,len(organised)):
    if i%14==0: 
        week=organised[start:start+14]
        weeklyData+=[week]
        start+=14
        week=[]
weeklyInf=0
weeklyInfArr=[]
for i in range(0,len(weeklyData)):
    for j in range(1,len(weeklyData[0]),2):
        weeklyInf+=weeklyData[i][j]
    print('week'+str(i+1)+'='+str(weeklyInf))
    weeklyInfArr+=[weeklyInf]
    weeklyInf=0
    
#list of days when infections>2000
badDays=[]#array of days with over 2000
for i in range(1,len(organised),2):
    if organised[i]>2000:
        badDays+=[organised[i-1]]
print(badDays)

#weekly percentage increment
print(weeklyInfArr)
wp=0#previous week
wc=0#current week
increment=0
for i in range(1,len(weeklyInfArr)):#
    increment=100*(weeklyInfArr[i]-weeklyInfArr[i-1])/weeklyInfArr[i-1]
    print('% increment= '+str(increment))
#week with max infections
Max=weeklyInfArr[0]
index=0
for i in range(0,len(weeklyInfArr)):
    if Max<weeklyInfArr[i]:
        Max=weeklyInfArr[i]
        index=i
print('week with most infections '+str(index+1))
    
    
        
    

