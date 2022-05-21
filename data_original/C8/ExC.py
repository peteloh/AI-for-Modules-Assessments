# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:16:13 2020


"""
"""CID 01726586"""

c=open('CV19.txt','r')
cov=c.readlines() #read the file
c.close()

cor=[]
for item in cov:
    cor+=[item.rstrip()] #remove newline /n sign from items

N=len(cor)
cor.pop(N-1)#the last item was an empty string
N=N-1 #length is 1 shorter
#want to make table of [week,date list,infection list] each is a list in a tuple
tup=[]
#each section has 1 week, 7 days, 7 infections = 15 items

#at the 0th,15th,30th position etc. the week is said
#list for just dates and infections
week=[]
for i in range(0,N):
    if i%15==0:
        week+=[cor[i]] #append every 15th index
        cor.pop(i)
        N=N-1
    dandi=cor #dandi is only dates and infections
      
#overall no. infections is sum of all infcetions
M=len(dandi)
toti=0 #total infections
ttdates=[]
for i in range(1,M+1,2): 
    #infections are at odd positions
    toti+=int(dandi[i])
    if int(dandi[i])>2000: #if infections on that day are above 2000
        ttdates+=[dandi[i-1]]  #list of days above 2000

#weekly infections
#for i in range()







        
        
        

        
        
        
        
        

    
    
    