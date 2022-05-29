#01730474
f = open('CV19.txt','r')
CV = f.readlines()
f.close()

N = 13
RN = range(0,N)
# organise data in a list of tuples
covid = [] 
c = 0
for i in RN:
    covid += [( CV[c].rstrip() , CV[c+1].rstrip() , int(CV[c+2].rstrip()), CV[c+3].rstrip() , int(CV[c+4].rstrip()),CV[c+5].rstrip() , int(CV[c+6].rstrip()),CV[c+7].rstrip() , int(CV[c+8].rstrip()),CV[c+9].rstrip() , int(CV[c+10].rstrip()),CV[c+11].rstrip() , int(CV[c+12].rstrip()),CV[c+13].rstrip() , int(CV[c+14].rstrip()) )] #seperate each week into its own tuple
    c += 15

sum=0
for item in covid:
    sum = sum + item[2]+ item[4]+ item[6]+ item[8]+ item[10]+ item[12]+ item[14] #sum the infections
print("total number of infections is " + str(sum))

