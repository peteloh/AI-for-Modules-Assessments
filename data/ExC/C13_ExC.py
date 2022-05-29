#My CID number is 01700084

filename = "CV19.txt"
file = open(filename, 'r')
values = []
for line in file:
    values.append(line)


print(len(values))
int_values =[]
for i in range(len(values)):
    if(i%2==0):
        int_values.append(line)


sum_of_total_case = 0
print(len(int_values))
for i in range(len(int_values)):
    sum_of_total_case = sum_of_total_case + int_values[i]


print(sum_of_total_case)