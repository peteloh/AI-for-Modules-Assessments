# CID: 01710404

f = open('CV19.txt','r')
t = f.readlines() # opening and reading ifle
f.close()

CV19 = []
for item in t:
    CV19 += [item.rstrip()] #stripping /n
    
CV19.pop(0)
CV19.pop(14)
CV19.pop(28)
CV19.pop(42)
CV19.pop(56)
CV19.pop(70)
CV19.pop(84)
CV19.pop(98)
CV19.pop(112)
CV19.pop(126)
CV19.pop(140)
CV19.pop(154) #removing week numbers
CV19.pop(168)

CV20 = []

while CV19 != []:
    CV20.append(CV19[:2]) # creating tuples of dates with their number of cases
    CV19 = CV19[2:]

CV20.pop(-1)
a = len(CV20)

DaysInfected = []

for i in range(0,a):
        if float(CV20[i][1]) > 2000: #traversing range to find indexes of the dates which have >2000 cases
            DaysInfected.append(i+1)

DaysInfected2 = []
    
for i in DaysInfected:
    DaysInfected2.append(CV20[i][0]) #adding these dates to a list

print('The days which had more than 2000 cases were: ',DaysInfected2)

Sum = 0

for i in range(0,a):
    Sum += float(CV20[i][1]) #adding each element in the 2nd column of the list

print('The number of infections in this period is: ',Sum)

CV21 = []

while CV20 != []:
    CV21.append(CV20[:7])
    CV20 = CV20[7:] # making new list with a tuple for each week containing tuples from each day
    
b = len(CV21)
Week = []
    
for i in range(0,b):
    Sum2 = 0
    for j in range(0,7):
        Sum2 += int(CV21[i][j][1]) # traversing list to add up each case from each day and summing for a week and adding to a list 
    Week += [Sum2]

print('The amount of infection per week is as follows: ',Week)

PercInc = []

for i in range(1,len(Week)):
    d = ((Week[i]-Week[i-1]) / Week[i-1] ) * 100 #using a formula for each index to find the percentage increase each weeek using the cases from each week in the week list
    PercInc.append(d)
    
print('The weekly percentage increment of infections is: ',PercInc)
    
HighWeek = max(Week)
c = Week.index(HighWeek) + 1 #using the max function to find highest amount of cases for each index and then using index to find the week

print('The week with the highest amount of infection is week',c)


