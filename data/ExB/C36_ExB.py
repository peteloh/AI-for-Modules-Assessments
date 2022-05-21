# Import functions needed
import matplotlib.pyplot as plot
import random

# Plot two circles
circle1 = plot.Circle((0,0),20,color='blue',fill=False)
circle2 = plot.Circle((0,0),10,color='blue',fill=False)
plot.gcf().gca().add_artist(circle1)
plot.gcf().gca().add_artist(circle2)
plot.axis([-25,25,-25,25])
plot.gca().set_aspect('equal')

# Move the ant
X = []
Y = []
Xstart = 0
Ystart = 18
Exit = False
while (Exit == False):
    X = X + [Xstart]
    Y = Y + [Ystart]
    dx = random.random()*2.4-1.8 #range is from -1.8 to 0.6
    dy = random.random()*2.4-1.8 #range is from -1.8 to 0.6
    Xstart = Xstart + dx
    Ystart = Ystart + dy
    # Bounce back if hits or goes beyond the wall 
    if (Xstart**2+Ystart**2)>=20**2 or (Xstart**2+Ystart**2)<=10**2:
        Xstart = Xstart - dx
        Ystart = Ystart - dy
    if (Ystart <= 0):
        Exit = True
    plot.plot(X,Y,c='red')


