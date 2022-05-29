#CID 01719854
#open the file
CV19=open('CV19.txt','r')
info=CV19.readlines()
#then get rid of the /n
N=len(info)
data=[]
R=range(0,N)
for i in R:
    data=data+[info[i].rstrip()]
print(data)
#create a list for each week
week1=[]
week2=[]
week3=[]
week4=[]
week5=[]
week6=[]
week8=[]
week9=[]
week10=[]
week11=[]
week12=[]
week13=[]
week1=data[1:15]
week2=data[17:30]
