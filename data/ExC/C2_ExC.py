

import matplotlib.pyplot as plt
import math
import random

#Opening the datafile for use throughout the script and storing in array
datafile = open("CV19.txt", "r")
data = datafile.readlines()
datafile.close()

'''Task C1'''
total = 0
#Iterate through each line and only count numbers (not dates or words)
for line in data:
    if not("Week" in line or "-" in line):
        total += int(line)
print("Total number of infections are:", total)


'''Task C2'''
#Weekly total function
def weekN(n, data):
    weeklyTotal = 0
    #Week starts on n-1 * 15th line and skips the date
    for line in data[(n-1)*15 + 2:(n*15):2]:
        weeklyTotal += int(line)
    return weeklyTotal

#output each week    
for i in range (1,14):
    print("Infections for week " + str(i) + ": " + str(weekN(i,data)))


'''Task C3'''







'''Task C4'''
def weeklyIncrement(n, data):
    return ((weekN(n, data) - weekN(n-1, data))/weekN(n-1, data)) * 100

for i in range(2,14):
    print("Weekly increment in % for week " + str(i) + ":" , str(weeklyIncrement(i, data)))