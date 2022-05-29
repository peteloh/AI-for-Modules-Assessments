# CID: 01720187

def read_file(file):
    f = open(file, "r")
    x = [str(line.rstrip()) for line in f.readlines()]
    f.close()
    return x

C = read_file("C:/Users/cdcch/Desktop/CV19.txt")

DAY = []
i = 0
accept = True
for item in C:
    if i % 15 == 0 or i == 0:
        i += 1
    elif accept:
        DAY += [(C[i], int(C[i+1]))]
        accept = False
        i += 1
    else:
        accept = True
        i += 1

total = 0
for i in range(len(DAY)):
    total += int(DAY[i][1])

print("1. Total infections:", total)

# N = number of weeks -1
N = 12
WEEK = []
i = 0
for week in range(N):
    WEEK += [(week +1, DAY[week*7][1]+DAY[week*7+1][1]+DAY[week*7+2][1]+DAY[week*7+3][1]+DAY[week*7+4][1]+DAY[week*7+5][1]+DAY[week*7+6][1])]
print("2. Weekly infections:", WEEK)

exceed = []
for i in range(len(DAY)):
    if DAY[i][1] > 2000:
        exceed += [DAY[i]]
print("3. Days of over 2000 infected:", exceed)

maxweek = 0
for i in range(len(WEEK)):
    if WEEK[i][1] > maxweek:
        maxweek = i
print("5. Week with highest infections:", WEEK[maxweek])