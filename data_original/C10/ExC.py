# Opening the text file and getting list from it
f = open('cv19.txt', 'r')
temp = f.readlines()
f.close()

#Turning list into strings with \n cut off
text = [i.rstrip() for i in temp]


# Overall number of infections
overall = 0 # Initialise overall infections
for i in text:
    if 0 < len(i) < 5:  # All infections have a digit >0 and <10000
        overall += int(i)



# Number of infections per week
def weekly(n):
    # Function that determined infections, where n is the week number
    week = 0
    for i in text[15 * (n-1): 15 * n]:
        if 0 < len(i) < 5:  # All infections have a digit >0 and <10000
            week += int(i)
    return week
week1 = weekly(2)


#3: infected above 2000
infecteddays = []
for i in text:
    if 0 < len(i) < 5:  # All infections have a digit >0 and <10000
        if int(i) > 2000:
            infecteddays.append(text[i-1]) # Day of infection is an index above on the list.