#01718219

f = open('CV19.txt','r')
temp = f.readlines()
f.close()

#number of weeks = len(temp)/15
#15 pieces of data per week
#13 weeks

Weeks = len(temp)/15
print(Weeks)

#loop for every week and display the week name and the sum of all cases for that week

Cases = []
Infections = []
for i in range(0,len(temp),13):
    Sum = 0
    for j in range(2,15,2):
         Sum = Sum + int(temp[j].rstrip())
    Infections = Infections + [sum]
    Cases = Cases + [(temp[i].rstrip(),Infections[i])]
    
#number of infections within the given period
Sum = 0
for i in range(0,13):
    Sum = Sum + [Cases[i][1]]
print(Sum)    

#weekly number of infections per every week period
for week in Cases:
    print(week)
    
    
#week with the highest number of infections

MaxWeek = Cases[0][0]
Max = Cases[0][1]
for i in range(1,13):
    if Cases[i][1] > Max:
        Max = Cases[i][1]
        MaxWeek = Cases[i][0]
        
#weekly percentage increment



    
    

    
    
        


    