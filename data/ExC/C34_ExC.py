# -*- coding: utf-8 -*-
"""
Question 3 Computing Exam


"""
def txt_to_list_tuples (filename, lines_per_tuple): #defines the function and input variables
    data = open(filename) #opens the file
    datavalues = data.readlines() #reads the data of the file and assignes it to variable datavalue
    data.close() #closes the file
    datavalues = [item.strip() for item in datavalues] #gets rid of any trailing information in datavalues list 
    output = [] #creates an empty list where outputs will be entered
    for i in range (0,len(datavalues),lines_per_tuple): #iterates through list in steps of lines per entry
        temptuple = (datavalues[i],datavalues[i+1],datavalues[i+2],datavalues[i+3],datavalues[i+4],datavalues[i+5],datavalues[i+6],datavalues[i+7],datavalues[i+8],datavalues[i+9],datavalues[i+10],datavalues[i+11],datavalues[i+12],datavalues[i+13],datavalues[i+14]) #if lines_per_entry=3 a temporary tuple is created from 1st,2nd and 3rd item in list. Change if number of line is not 3
        output.append(temptuple) #this tuple then appended to output list
    return output #output list is returned

#task 1
def TotalInfections ():
    inputlist = txt_to_list_tuples('CV19.txt',15) #creates list of tuples tuple from input file
    totalinfections = 0 #sets counter to 0 for total infections
    for i in range (len(inputlist)): #iterates through list
        for j in range (2,len(inputlist[0]),2): #iterates through indiviual tuples in steps of 2 from 2 as weekly cases occur on 2nd,4th,6th etc... indicies only
            totalinfections += int(inputlist[i][j]) #adds cases to total infections counter
    return totalinfections #returns total infections
#task 2
def WeeklyInfections ():
    inputlist = txt_to_list_tuples('CV19.txt',15) #creates list of tuples tuple from input file
    WeeklyInfections = [] #creates an empty list of weekly infections
    ThisWeeksInfections = 0 #creates temporary counter for this weekly infectiosn
    for i in range (len(inputlist)): #iterates through input list
        for j in range (2,len(inputlist[0]),2):#iterates through indiviual tuples in steps of 2 from 2 as weekly cases occur on 2nd,4th,6th etc... indicies only
            ThisWeeksInfections += int(inputlist[i][j]) #adds this weeks infections to temporary counter
        WeeklyInfections.append(ThisWeeksInfections) #appends counter value to WeeklyInfections list
        ThisWeeksInfections =0 #clears counter for subsequent weeks
    for i in range (len(WeeklyInfections)): #goes through the WeeklyInfections list and prints weekly infections and the week they occured
        print ('On week ' + str((i+1)) + ' there were ' + str(WeeklyInfections[i]) + ' infections')

#task 3
def DaysWhereInfectionsExceed2000 ():
    inputlist = txt_to_list_tuples('CV19.txt',15) #creates list of tuples tuple from input file
    Days = [] #creates empty list of days where infections exceed 2000
    for i in range (len(inputlist)): #iterates throguh list
        for j in range (2,len(inputlist[0]),2): #iterates through indiviual tuples in steps of 2 from 2 as weekly cases occur on 2nd,4th,6th etc... indicies only
            if int(inputlist[i][j])>2000: #if caseses exceed 2000
                Days.append(inputlist[i][j-1]) #the day is appended to days list. The day is 1 indicie less than daily infection on that day hence -1
    print (Days) #prints days
#task 4
def WeeklyInfectionsListMaker ():
    inputlist = txt_to_list_tuples('CV19.txt',15)
    WeeklyInfections = [] 
    ThisWeeksInfections = 0
    for i in range (len(inputlist)):
        for j in range (2,len(inputlist[0]),2):
            ThisWeeksInfections += int(inputlist[i][j])
        WeeklyInfections.append(ThisWeeksInfections)
        ThisWeeksInfections =0
    return WeeklyInfections #same script as task 2 but outputs list rather than printing it out


def WeeklyPercentageIncrements():
    WeeklyInfections = WeeklyInfectionsListMaker()
    for i in range (1,len(WeeklyInfections)):
        increment = (int(WeeklyInfections[i])-int(WeeklyInfections[i-1]))/(int(WeeklyInfections[i-1]))*100
        print (str(increment) + ' %') #uses formula on question and iterates through list missing out first value as instructed

#task 5
def WeeklyInfectionsHeadless ():
    inputlist = txt_to_list_tuples('CV19.txt',15)
    WeeklyInfections = []
    ThisWeeksInfections = 0
    for i in range (len(inputlist)):
        for j in range (2,len(inputlist[0]),2):
            ThisWeeksInfections += int(inputlist[i][j])
        WeeklyInfections.append(ThisWeeksInfections)
        ThisWeeksInfections =0
    return WeeklyInfections #same script as task 2 but outputs list rather than printing it out

def MaxNumberInfections():
    WeeklyInfections = WeeklyInfectionsHeadless() #list weekly infections
    MaxInfections = max(WeeklyInfections) #finds max infections
    MaxInfectionsDay = (WeeklyInfections.index(max(WeeklyInfections)))+1 #finds index of max infections and adds 1 to find correct day
    print ('Week ' + str(MaxInfectionsDay) + ' had the maximum number of infections at ' + str(MaxInfections)) #outputs value
    
