#CID: 01702304

# read in file
f = open('CV19.txt','r')
t = f.readlines()
f.close()

# define function Sum(N) where N is week number
def Sum(N):
    s = 0
    R = range((15*N-13),(15*N+1),2)
    for i in R:
        s = s + int(t[i])
    return s

# caclulate total number of infections over the 13 week period
s = 0
N = 13
R = range(1,N+1)
for j in R:
    s = s + Sum(j)
print('the total number of infections were ' + str(s))

# calculate total number of infections per week
c=[]
s = 0
N = 13
R = range(1,N+1)
for j in R:
    s = Sum(j)
    print('for week ' + str(j) + ' there were ' + str(s) + ' infections')
c = c + [s]
print(c)
    
# calculate days when infections exceeded 2000
#define function for exceeding 2000
def exc(N):
    c = 0
    R = range((15*N-13),(15*N+1),2)
    for i in R:
        if int(t[i]) > 2000:
            c = c + 1
            print(t[i-1]) # print the date of the day when infections over 2000
            
#main script
c = 0
N = 13
R = range(1,N+1)
for j in R:
    c = exc(j)



N = len(s)
R = range(0,N)
for i in R:
    Rs = range(1+i,N)
    for j in Rs:
        if s[j] < s[i]:
            (s[j],s[i]) = (s[i],s[j])


