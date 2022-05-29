def increment(new, old):
    diff = float(new-old)
    return str((diff/float(old)) * 100) + '%'

def extractData():
    file = open("CV19.txt")
    lines = file.readlines()
    weeks = []
    greater_than_2000 = []
    total = 0
    week_num = -1
    day = str()

    for line in lines:
        if str(line)[0] == 'W':
            week_num += 1
            weeks.append(0)
            continue
        if len(str(line)) > 8:
            day = str(line).strip()
            continue
        
        num_infection = int(line)
        if num_infection > 2000:
            greater_than_2000.append((day, num_infection))

        weeks[week_num] += num_infection
        total += num_infection
    
    file.close()
    print("Overall Number of Infections: " + str(total))
    print("Weekly Numbers:")
    for i,x in enumerate(weeks):
        print("\tWeek " + str(i+1) + ": " + str(x))
    print("Days exceeding 2000: ")
    for day, num in greater_than_2000:
        print("\t" + day + ": " + str(num))
    print("Weekly percentage increment:")
    for i in range(len(weeks) - 1):
        print("\tWeek " + str(i+1) + " - " + str(i+2) + ": " + increment(weeks[i+1], weeks[i]))
    print("Week with highest number of infections: ")
    max_week_infection = max(weeks)
    print("\tWeek " + str(weeks.index(max_week_infection)) + ": " + str(max_week_infection))

extractData()