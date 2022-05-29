#CID = 01712921


# read file
f = open('CV19.txt','r')
t = f.readlines()
f.close()


f = open('CV19.txt','r')
t = f.readlines()
f.close()
N = 91
RN = range(0,N)
# organise data in a list of tuples
Covid = [] # list of companies
c = 0
w = 0
for i in RN:
    Covid += [( t[0].rstrip() , t[c+1].rstrip() , t[c+2].rstrip() )]
    w += 1
    c += 2


print(Covid)


#wasnt able to import the text file split up into a tuple of [(week),(date),(infected)] so couldnt do the rest of the question :(





























