#MEHCH40008

#Computing Exam

#CID: 01704200


#Question 3

#open and read the file, input every element as stripped into an elements list and close the file
file = open('CV19.txt', 'r')
elements = []
for i in file:
    elements.append(i.rstrip())
#print(elements)
file.close()

#part 1
#create a counter so as to exclude the first week number and day number and a sum variable
i = 2
TotalInfections = 0
#traverse the elements list
while i < len(elements):
    #traverse each week
    for j in range(0, 7):
        #add the number of infected to the total sum
        TotalInfections += int(elements[i])
        #increment the counter by 2 so as to skip the date element
        i += 2
    #after each week increment the counter by 1 so as to skip the week number
    i += 1
print('The total number of infections registered in given period is: ' + str(TotalInfections))

#part 2
#create a counter and a weekly infections list
i = 0
WeeklyInfections = []
#traverse the elements list
while i < len(elements):
    #create a variable containing the week numbern and a sum variable for all the infections in that week
    week = elements[i]
    infections = 0
    #traverse each week
    for j in range(0, 7):
        #increment the counter by 2 so as to skip the date element
        i += 2
        #add the number of infected to the total sum
        infections += int(elements[i])
    #increment the counter by 1 to go to the next element
    i += 1
    #add the week number and total infections of that week into a tuple and append it to the weekly infections list
    WeeklyInfections.append((week, infections))
print('The weekly number of infections per every week provided is: ' + str(WeeklyInfections))

#part 3
#create a counter so as to exclude the first week number and day number and a list of days when the number of infections exceeded 2000
i = 2
BadDays = []
#traverse the elements list
while i < len(elements):
    #traverse each week
    for j in range(0, 7):
        #if the total infected that day exceeds 2000 add the day into the bad day list
        if int(elements[i]) > 2000:
            BadDays.append(elements[i - 1])
        #increment the counter by 2 so as to skip the date element
        i += 2
    #after each week increment the counter by 1 so as to skip the week number
    i += 1
print('The days when the number of infected people exceeded 2000 were: ' + str(BadDays))

#part 4
#create a counter so as to exclude the first week and a percentage increment list
i = 1
increment = []
#traverse the weekly infections list
while i < len(WeeklyInfections):
    #find the increment
    inc = 100 * (WeeklyInfections[i][1] - WeeklyInfections[i - 1][1]) / WeeklyInfections[i - 1][1]
    #append the week number and the increment as a tuple to the percentage increment list
    increment.append((WeeklyInfections[i][0], inc))
    i += 1
print('The weekly percentage increment of infections is: ' + str(increment))

#part 5
#create a list with the weekly infections only
weekinf = []
#traverse the list of both weekly infections and week number and append the first to the new list
for i in range(0, len(WeeklyInfections)):
    weekinf.append(WeeklyInfections[i][1])
#find the highest number of infections
WorstInfections = max(weekinf)
#traverse the list of weekly infections with week numbers and look for the week that has the highest number of infections
for i in range(0, len(WeeklyInfections)):
    if WorstInfections == WeeklyInfections[i][1]:
        WorstWeek = WeeklyInfections[i][0]
print('The week with the highest number of infections was: ' + WorstWeek)