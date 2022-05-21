#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:46:33 2020


"""

# CID: 01720439

x = open("CV19.txt")    #Opening file
temp = x.readlines()    #assigning contents to an array
x.close()   #closing file for good practicee

p = []  #empty array that will be filled out

for i in range (0,len(temp)):
    p.append(temp[i].rstrip())  #setting contents of file to an array p, removing \n

p.pop() #removing unnecesary last blank term

print(p)



for i in range(0,13): #Traversing through weeks
    for j in range(1,8): #Traversing through days
        Sum += int(p[i * 15 + j * 2]) #total in all time
        
print("The overall number of infections registered in the given period is: " + str(Sum))
print(" ")



weektotals = []
for i in range(0,13):#Traversing through weeks
    Total = 0 #total for week
    for j in range(1,8):#Traversing through days
        Total += int(p[i * 15 + j * 2])
    weektotals += [Total] #adding to weektotals, for use in later increment analysis
    print("The overall number of infections in Week " + str(i+1) + " is: " + str(Total))
print(" ")



days = []
for i in range(0,13): #Traversing through weeks
    for j in range(1,8): #Traversing through days
        if int(p[i * 15 + j * 2]) > 2000: #if cases exceed 2000
            days += [p[(i * 15 + j * 2)-1]] #adding preceeding date to list of days
print("The list of days when the number of infected people exceeded (>) 2000 is: ")
print(days)
print(" ")



for i in range (1,len(weektotals)): #for loop printing and conducting calculation simultaneosly, pulling data from weektotals list
    print("increment in week " + str(i+1) + " " + str(((weektotals[i]-weektotals[i-1])/weektotals[i-1])*100))
print(" ")


Max = 0 #initialising max
date = 0 #initializing date

for i in range(0,13): #Traversing through weeks
    for j in range(1,8): #Traversing through days
        if int(p[i * 15 + j * 2]) > Max: #combs through all values, changing values for every number greater than the current max
            date = p[(i * 15 + j * 2)-1] #will register the date of the max number in the variable after all elements sifted through
            Max = int(p[i * 15 + j * 2])

print("The maximum number of cases was: " +str(Max) + " on the date: " + date)
        