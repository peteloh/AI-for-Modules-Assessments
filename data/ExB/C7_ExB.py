# The ant's movement pattern
Antx = [0]
Anty = [18]

# The ant's position at a particular time 

x = 0 
y = 18

# Define s1 and s2
s1 = -((1/10) + 0.9)
s2 = (5/10) + 0.6 

import random 
import matplotlib.pyplot as pl

# Set the ant's condition
Green = False

# Start the ant's movement 

# Run whilst the Ant is in the red zone
while not Green:
    
    # Compute dx and dy 
    dx = s1 + (random.random())*(s2-s1) 
    dy = s1 + (random.random())*(s2-s1) 
    
    # If ant has hit a wall, compute x and y again
    if (x+dx)**2 + (y+dy)**2 >= 400 or (x+dx)**2 + (y+dy)**2 <= 100: 
        continue
    else: 
        # Compute new x and y 
        x += dx 
        y += dy 
        # Add to plot 
        Antx += [x]
        Anty += [y]
        
    # Check if reached green zone
    if 10 < abs(x) < 20 and y < 0:
        
        Green = True 

pl.(Antx,Anty)