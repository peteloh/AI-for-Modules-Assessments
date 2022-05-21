#Task C 
# CID Number: 01739141

covid_file = open('CV19.txt','r')
total_number = 6
dates = []
m = 3
d = 1
while m <= 5:
    while d <= 31:
        if d <10:
            dates.append(str('2020-0'+ str(m)+'-0'+ str(d)))
        else:
            dates.append(str('2020-0'+ str(m)+'-'+ str(d)))
        d+=1
    d = 1
    m +=1
weeks = []
w = 1
while w <=13:
    weeks.append('Week '+str(w))
    w +=1
    
#Part 1    
for line in covid_file:
    ind1= line.find('/n')
    value = line[:ind1]
    if not (value in weeks or value in dates):
        a = int(value)
        total_number += a
print(total_number)
covid_file.close() 

#Part 2 
covid_file = open('CV19.txt','r')
count = 0 
week = 1
total_week_number = 0
for i in range(13):
    while count <= 7: 
        for line in covid_file:
            ind1= line.find('/n')
            value = line[:ind1]
            if not (value in weeks or value in dates):
                count += 1
                a = int(value)
                total_week_number += a
        print( 'Week '+ str(week) + ' count :' + str(total_week_number))
week +=1
count = 0 
total_week_number = 0 
        
covid_file.close() 
#Part 3  
covid_dict = {}
for line in covid_file:
    ind1= line.find('/n')
    value = line[:ind1]
    if not (value in weeks):
        covid_dict


covid_file.close() 

