# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:57:19 2020




# CID: 01506597

# open the file CV19.txt
f=open("CV19.txt","r")
CV19=f.readlines()
f.close()


# get rid of the "\n" after every term
i=0
for item in CV19:
    mk=item.rstrip()
    CV19[i]=mk
    i=i+1


# L is the same list as CV19 but without each "Week X" term, to make indexing easier
L=[]
for i in range(len(CV19)):
    if int(i/15)!=i/15:
        L=L+[CV19[i]]
    else:
        L=L


# this transforms the number of infections values from strings to integers
for i in range(len(L)):
    if int(i/2)==i/2:
        L[i+1]=int(L[i+1])



# sum all the infections
s=0
for i in range(len(L)):
    if int(i/2)==i/2:
        s=s+L[i+1]
# s is the total number of infections over the period
print(s)
# s=273319







# Weekly number of infections:

# P is a list containing all the daily infections 
P=[]
for i in range(len(L)):
    if int(i/2)==i/2:
        P=P+[L[i+1]]

# M is a matrix containing a list of the number of infections each day, for each week
M = []
count = 0
for r in range(13):
    row = []
    for c in range(1,8):
        row = row  + [P[count]]
        count = count + 1
    M=M+[row]

W=[]
for i in range(len(M)):
    W=W+[0]
    for j in range(len(M[0])):
        W[i]=W[i]+M[i][j]

print(W)
# W is a list where each term if the number of weekly infections 
# W=[241, 1118, 3623, 12075, 24814, 37088, 35226, 34160, 33883, 33000, 24901, 17518, 15672]


# List of days when infections>2000
L1=[]
for i in range(len(P)):
    if P[i]>2000:
        L1=L1+[P[i]]

print(L1)


# Week with highest number of infections:
h=W[0]
for i in range(len(W)):
    if W[i]>h:
        h=W[i]

# h is the highest number of weekly infections, it is for week 6
print(h)
print(6)