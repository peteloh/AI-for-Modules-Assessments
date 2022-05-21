#CID:01702139
#1
f=open('CV19.txt','r')
a=f.readlines()
f.close()

N=13             #Number of cases found in week 1
cases1=0
for i in range(2,N+2,2):
    cases1=cases1+int(a[i])
print(cases1)

for j in range(0,len(a),13):       #Trying to create a loop to evaluate all the cases for all weeks in a.
    cases=0                  
    for i in range(j+2,J+N+2,2):
        cases=cases+int(a[i])
print(cases)

#2
Sum=0

