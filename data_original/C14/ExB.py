# start by stating my CID for the examiner, which I shall do while assigning it to a variable as a string
cid = '01501086'

# import libraries
import random
import math
# just realised I don't have matplotlib installed so I may try to fix this later. For now, I'll try to write the rest of the code
# but it shall be tricky as I can't really troubleshoot or see what's going on. I'll put pyplot code in as comments so the
# code still compiles and doesn't keep throwing error messages saying it doesn't know what matplotlib is
# import matplotlib.pyplot as plt

# Task B

# define s1 and s2 as floating point numbers
s1 = float((1/10)+0.9) # remember to make this number negative when used
s2 = float((8/10)+0.6)

# define the inner and outer radii of the donut
innerRadius = 10
outerRadius = 20

# create a list to store the ant's position
position = [[0],[18]]

# run the program inside a while loop so that it stops once the ant is at or below y = o
while position[1][-1] >= 0:
    dx = random.uniform(-s1,s2)
    dy = random.uniform(-s1,s2)
    # determine radius of new point
    radius = math.sqrt((position[0][-1]+dx)**2 + (position[1][-1]+dy)**2)
    if radius > innerRadius and radius < outerRadius:
        # then the ant is still within the donut so save this new position. If it isn't within the donut, then this
        # if statement won't trigger and the while loop shall just restart, creating a new dx and new dy as it does so
        position[0] += [position[0][-1]+dx]
        position[1] += [position[1][-1]+dy]

# plot the ant's path
# obviously this won't work as I don't have matplotlib installed but I'll write out the code anyways
# plt.plot(position[0],position[1])