import random, matplotlib.pyplot as plt, math

def move():
    xPoints = []
    yPoints = []
    antX = 0
    antY = 18
    s1 = 2/10 + 0.9
    s2 = 5/10 + 0.6
    xPoints.append(antX)
    yPoints.append(antY)
    
    while(not testGreen(antX, antY)):
        prevX = antX
        prevY = antY
        dx = random.uniform(-s1, s2)
        dy = random.uniform(-s1, s2)
        antX = antX + dx
        antY = antY + dy
        if(not testPosition(antX, antY)):
            antX = prevX
            antY = prevY
        xPoints.append(antX)
        yPoints.append(antY)

    print(antX)
    
    #using a graph
    x = xPoints
    y = yPoints
    plt.axis([-20,20,-20,20])
    plt.scatter(x,y)

def testPosition(x, y):   # Tests if ant is in annulus
    hyp = math.sqrt(x**2 + y**2)
    return (10 <= hyp <= 20)
  
def testGreen(x, y):
    return y < 0 and testPosition(x, y)

move()               # Runs program

    
    