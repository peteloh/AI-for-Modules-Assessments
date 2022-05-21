#01702538

#Note: 2 empty lines were left at the end of the text file
#Hence, this would affect some calculations using len()
#So, I removed them on my end


def CV():
    a = open('CV19.txt','r')
    b = a.read().splitlines()
    a.close()
    #15 elements per week
    W = 15
    c = 0
    #Total sum
    TS = 0
    #Weekly infections
    WI = []
    #Days exceeding 2000
    DE = []
    while c < len(b):
        #Sum each weeks infections
        WS = 0
        for i in range(0,W):
            if i == 0:
                TS += 0
            #odd values refer to the date
            elif (i%2) != 0:
                TS += 0
            else:
                #
                TS += float(b[c])
                WS += float(b[c])
                #if it exceeds 2000
                if float(b[c]) > 2000:
                    #date is the element behind the infections ~ c-1 
                    DE.append(b[c-1])
            c += 1
        WI.append(WS)
    
    #Weekly percentage increment
    WPI = []
    for n in range(1,len(WI)):
        Percentage = (WI[n]-WI[n-1])/(WI[n-1]) *100
        WPI.append(Percentage)
    
    Max = max(WI)
    
#    print(TS)
#    print(WI)
#    print(DE)
#    print(WPI)
#    print(Max)
    
CV()