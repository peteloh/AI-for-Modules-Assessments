#TaskC CID 01742057

#stripping the lines from a txt file
CV19fromfile = open("CV19.txt").readlines()
CV19 = []
for line in CV19fromfile:
    line = line.rstrip("\n")
    line = str(line)
    CV19.append(line)


covid = CV19
#remove all the string label for the week
for i in range(0,13):
    covid.remove(covid[14*i])
    


infections = 0
#add the values of everyother element
for i in range(0,int(len(covid)*0.5)):
    infections = infections + int(covid[(2*i)+1])
print(infections)
print(covid)
print(len(covid)*0.5)

infectionlist = []
for i in range(0,int((len(covid)*0.5))):
    infectionlist.append(covid[(2*i)+1])
print(infectionlist)
print(len(infectionlist))

weeklyinfections = []
for j in range(0,12):
    sum = 0
    for i in range(0,7):
        sum = sum + int(infectionlist[(7*j)+i])
    weeklyinfections.append(sum)
print(weeklyinfections)