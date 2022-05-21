# TaskB
import random
import matplotlib.pyplot as plt
CID = [0, 1, 7, 0, 3, 0, 8, 7]
#Initial position
xp = 0
yp = 18

# S values using my CID
s1 = 3 / 10 + 0.9
s2 = 8 / 10 + 0.9


# Lists x,y to plot position
x = [0]
y = [18]
notEscaped = True   # loop only stops when y < 0
while notEscaped:
    dx = random.randrange(-10 * s1, int(10 * s2), 1) / 10  # Random number with precision 0.1 between -s1, and s2
    dy = random.randrange(-10 * s1, int(10 * s2), 1) / 10  # Same
    # Moves position of the ant
    xp += dx
    yp += dy
    if  20**2 <= ((xp)**2 + (yp)**2 )<= 10**2:      # Setting the boundaries
        # Moving back to previous position
        xp -= dx
        yp -= dy
    # Placing values in list
    x += [xp]
    y += [yp]
    # Exit code
    if yp <= 0:
        notEscaped = False

#Plotting graph
plt.scatter(x,y)


