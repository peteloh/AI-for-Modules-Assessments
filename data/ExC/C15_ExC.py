#Task C
#Process:
#read the covid-19 file
#1) Weeks are every 15th position from the start
#2) Use a range to eliminate every 15th position, leaving just alternating days and infections
#3) using a range to sum every other element (the number of infections)


#open the file, read it as Cases
fc = open('CV19.txt','r')
Cases = fc.readlines()
fc.close()

    
N = len(Cases)
Rw = range(1,N,15)
A = []


#the range (1,N,15) = 1, 16, 31
#when the position of elements in cases = the position 1, 16, 31, should ignore it
#if it does not, add it to the list
for i in Cases:
    A = []
    
    for j in Rw:
        if Cases[i] != [j]:
            A = Cases[i]
            
#then can take every other element of the list, the no. of infections and can add them together 