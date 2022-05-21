# start by stating my CID for the examiner, which I shall do while assigning it to a variable as a string
cid = '01501086'

print(cid)

# Task C

# open the file, save the data to a list and then close the file
f = open('CV19.txt','r')
a = f.readlines()
f.close()
print(a)

# move the data to a new list where it will be nicely organised
# first sublist for weeks, second sublist for dates, third sublist for number of infections
data = [[],[],[]]
for i in range(0,len(a),15):
    for j in range(0,7):
        data[0] += [str(a[i])[:-1]]
        data[1] += [str(a[1+i+(2*j)])[:-1]]
        data[2] += [int(a[2+i+(2*j)])]

print('printing data columns separately')
print(data[0])
print(data[1])
print(data[2])


# find the total number of infections
totalInfections = 0
for i in data[2]:
    totalInfections += i

print('printing total number of infections')
print(totalInfections)


# find weekly infections
for i in range(0,13):
    print('printing number of infections in week ' + str(i+1))
    weeklyInfections = 0
    for j in range(0, 7):
        weeklyInfections += data[2][i+j]
    print(weeklyInfections)


# find days when more than 2000 infected
listDays = []
for i in range(0,len(data[0])):
    if data[2][i] > 2000:
        listDays += [data[1][i]]
print('printing list of days when more than 2000 infected')
print(listDays)


# finding weekly increment
