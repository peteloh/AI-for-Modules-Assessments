# Solution for Task C
# My CID Number: 01366896

import math as mt

# open the file for reading
f = open('CV19.txt','r')
t = f.readlines() # save data initially into a temporary variable t
f.close() # close the file

# no of weeks N = 13
N = 13
RN = range(0,N)

# organise data in a list of tuples - import data from file into a list
CovidStats = [] # list of weeks - data type: list of tuples
c = 0
for i in RN:
    # Week #, Day #, Stat # - 7 days per week
    CovidStats += [( t[c].rstrip() , 
                    t[c+1].rstrip() , int(t[c+2].rstrip()) ,
                    t[c+3].rstrip() , int(t[c+4].rstrip()) , 
                    t[c+5].rstrip() , int(t[c+6].rstrip()) , 
                    t[c+7].rstrip() , int(t[c+8].rstrip()) ,
                    t[c+9].rstrip() , int(t[c+10].rstrip()) ,
                    t[c+11].rstrip() , int(t[c+12].rstrip()) ,
                    t[c+13].rstrip() , int(t[c+14].rstrip()) ,
                   )] 
    c += 15
#

# We have created a list of tuples!
#print(type(CovidStats))
#print(type(CovidStats[0]))
#for i in CovidStats:
#    print(i)

# Find the following:
# 1. The overall number of infections registered in the given period
# 2. The weekly number of infections per every week provided
# 3. The list of days when the number of infected people exceeded (>) 2000
# 4. The weekly percentage increment of infections (apart from week 1)
# 5. The week with the highest number of infections

# compute the weekly number of infections
WeekS = []
C = 0
for i in RN:
    Sum = 0
    for j in R2:
        WeekS += [Sum[i][c]] 
        print(S)
print("Overall Weekly Infections: " + str(S))

# compute the overall number of infections
# concept would be to sum up the number of weekly infections found earlier
S = 0 # initialise sum = 0
for i in RN:
    R2 = range(0,14,2)
    for j in R2:
        S += CovidStats[i][c] 
        print(S)
print("Overall Number of Infections: " + str(S))


# list of days when number of infected people (>) 2000

                ]
ListDays = []
C = 0
for i in RN:
    for j in R2:
        #this is the concept but I did not have time to implement it
        if Inf > 2000:
            ListDays += [Day
print("Overall Weekly Infections: " + str(S))

# Percentage increment
# W(n) is the number of infections in week n and W(n-1) is the number of infections in the previous week
PercentIncre = (W(n) - W(n-1) / W(n-1)) * 100

# Week with highest number of infections
MaxInf = 0
for i in RN:
    if Inf > MaxInf:
        MaxInf = Inf
print("Week with most infections: " + str(MaxInf))
