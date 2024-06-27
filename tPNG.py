# Plot the height function of tpng at location (

import numpy as np
import matplotlib.pyplot as plt
import bisect

def simulate_height(t, x, y):
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
        if t < 1:
            numJumps = np.random.geometric(1-t, size=None)
        elif t == 1:
            numJumps = len(particleLocations) - index
        if index + numJumps > len(particleLocations) - 1:
            height += 1
        else:
            endPoint = particleLocations[index+ numJumps]
            particleLocations.remove(endPoint)
    return height
    
def plot(t, x, y):
    xMin = 0
    xMax = x
    yMax = y
    time = 0
    particleLocations = []
    iters = 0
    lines_to_plot = []
    while(time < yMax):
        iters += 1
        oldTime = time
        time += np.random.exponential(scale=1/(xMax - xMin), size=None)

        # move old particle up to new time (draw vertical segment)
        for i in range(len(particleLocations)):
            lines_to_plot.append([particleLocations[i], particleLocations[i]]) # x
            lines_to_plot.append([oldTime, time]) # y
            lines_to_plot.append('k') 

        # add new particle at location
        location = np.random.uniform(low=xMin, high=xMax, size=None)

        index = bisect.bisect(particleLocations, location)
        particleLocations.insert(index, location)

        # sample geometric distribution
        if t < 1:
            numJumps = np.random.geometric(1-t, size=None)
        elif t == 1:
            numJumps = len(particleLocations) - index
        if index + numJumps > len(particleLocations) - 1:
            endPoint= xMax
        else:
            endPoint = particleLocations[index+ numJumps]
            particleLocations.remove(endPoint)
        # draw horizontal segment
        lines_to_plot.append([location,endPoint]) # x
        lines_to_plot.append([time, time]) # y
        lines_to_plot.append('k')
    return lines_to_plot
    



    


    