# read the file
f = open('FTSE100.txt','r')
t = f.readlines()
f.close()
N = 100
RN = range(0,N)
# organise data in a list of tuples
FTSE = [] # list of companies
c = 0
for i in RN:
    FTSE += [( t[c].rstrip() , float(t[c+1].rstrip()) , int(t[c+2].rstrip()) )]
    c += 3
#
# sort the list in descending order by share price
for i in RN:
    Rj = range(i+1,N)
    for j in Rj:
        if FTSE[i][1] < FTSE[j][1]:
            # swap these two companies
            (FTSE[i], FTSE[j]) = (FTSE[j], FTSE[i])
for item in FTSE:
    print(item)
# 
# compute the overall value of the FTSE companies
S = 0
for i in RN:
    S += FTSE[i][1]*FTSE[i][2]
# convert in billion dollars
S = S / 1.0e9
print(S)