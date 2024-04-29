# Plot the height function of tpng at location (

import numpy as np
import matplotlib.pyplot as plt
import bisect

def heightTPNG(q, x, y):
    xMin = 0
    xMax = x
    yMax = y
    time = 0
    particleLocations = []
    height = 0
    while(time < yMax):
        oldTime = time
        time += np.random.exponential(scale=1/(xMax - xMin), size=None)

        # add new particle at location
        location = np.random.uniform(low=xMin, high=xMax, size=None)
        index = bisect.bisect(particleLocations, location)
        particleLocations.insert(index, location)

        # sample geometric distribution
        if q < 1:
            numJumps = np.random.geometric(1-q, size=None)
        elif q == 1:
            numJumps = len(particleLocations) - index
        if index + numJumps > len(particleLocations) - 1:
            height += 1
        else:
            endPoint = particleLocations[index+ numJumps]
            particleLocations.remove(endPoint)
    return height

# Plot the normalized height function at (n, n) as a function of q, compare with the theoretical limit 2/\sqrt{1-q}   

n = 500
m = 100
x_val = np.linspace(0.05, 0.95, m+1)
y_val = np.empty(m+1)
for i in range(m+1):
    q = 0.05 + 0.9/m*i
    y_val[i] = heightTPNG(q, n, n)/n


fig, ax = plt.subplots(1, 1, figsize = (5, 5))
ax.plot(x_val, y_val, 'b')
ax.plot(np.linspace(0.05, 0.95, m+1), 2/np.sqrt(1-np.linspace(0.05, 0.95, m+1)), 'r')
