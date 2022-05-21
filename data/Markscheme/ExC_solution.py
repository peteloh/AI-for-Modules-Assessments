# Ex 3 prep
f = open('days.csv','r')
d = f.readlines()
f.close()
f = open('infections.csv','r')
m = f.readlines()
f.close()
print(len(d))
ll = []
w = 1
for i in range(0,len(d)):
    if i%7 == 0:
        ll += ['Week '+str(w)]
        w += 1
    ll += [d[i][0:10]]
    ll += [m[i].rstrip()]
    

f = open('CV19.txt','w')
for item in ll:
    f.write(item+'\n')
f.close()   

# Ex 3
import matplotlib.pyplot as pl
# read the file
f = open('CV19.txt','r')
t = f.readlines()
f.close()
# length of data
N = len(t)

# organise the data
day = [] # dates
infect = [] # number of infections of the day
# examine all the data read in, line by line
for i in range(0,N):
    # check if this line is the start of a new week
    if i%15 == 0:
        # start a new week
        c = 1
    else:
        # same week, import date of the day and number of infections of the day
        if c%2 == 1:
            # this line contains the date of the day
            day += [t[i].rstrip()]
        else:
            # this line contains the number of infections
            infect += [int(t[i].rstrip())]
        c += 1

# number of days
Nd = len(day)

# analyse data
tot = 0 # overall number of infections
days2000 = [] # list of days with high infections (>2000)
infectw = [] # number of infections per week

totw = 0
# scroll data, day by day
for i in range(0,Nd):
    tot += infect[i] # update overall infections 
    # check if this day had high infections (>2000)
    if infect[i]>2000:
        # yes, add this date to the list of high infections
        days2000 += [day[i]]
    
    # compute weekly number of infections
    # add this number of infections to the weekly total
    totw += infect[i]  # add the number of infection to this week
    # check if end of week
    if (i+1)%7 == 0:
        # store the weekly total
        infectw += [totw]
        # reset the weekly total
        totw = 0




# analyse weekly data
Nw = len(infectw)
ratew = [] # weekly rate of infections
maxw = infectw[0]  # number of infections in a week
week = ['1'] # start assuming teh first week had highest number
# scroll the weekly data
for i in range(1,Nw):
    if infectw[i] > maxw:
        # this week has a highest numebr of infections
        # updatethe maximum
        maxw = infectw[i]
        # update the week
        week = str(i+1)
    # compute the rate for this week
    ratew += [(infectw[i]-infectw[i-1])/infectw[i-1]*100]

# print results
print(tot)
print(infectw)
print(len(days2000))
print(days2000)
print(ratew)
print(week)
pl.plot(range(0,Nd),infect)