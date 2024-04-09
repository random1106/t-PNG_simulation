import numpy as np
import matplotlib.pyplot as plt
import bisect

#WindowSize
xMin=0;xMax=12
yMin=0;yMax=12

#Choose the q parameter in [0,1]

def plotTPNG(q):
  time = 0
  particleLocations = []
  iters = 0
  lines_to_plot = []
  while(time < yMax):
    iters += 1
    oldTime = time
    time += np.random.exponential(scale=1/(xMax - xMin), size=None)
    #print("time", time)
    #move old particle up to new time
    for i in range(len(particleLocations)):
      # plt.plot([particleLocations[i], particleLocations[i]], [oldTime, time], 'k')
      lines_to_plot.append([particleLocations[i], particleLocations[i]]) # x
      lines_to_plot.append([oldTime, time]) # y
      lines_to_plot.append('#000000')# format

    #add new particle at location
    location = np.random.uniform(low=xMin, high=xMax, size=None)
    #print("location", location)

    index = bisect.bisect(particleLocations, location)
    particleLocations.insert(index, location)
    # particleLocations.append(location)
    # particleLocations.sort()
    # index = particleLocations.index(location)

    #sample geometric distribution
    if q < 1:
      numJumps = np.random.geometric(1-q, size=None)
    elif q == 1:
      numJumps = len(particleLocations) - index
    #plt.scatter(location,time, color= '#0000ff')
    if index + numJumps > len(particleLocations) - 1:
      endPoint= xMax
    else:
      endPoint = particleLocations[index+ numJumps]
      particleLocations.remove(endPoint)

    lines_to_plot.append([location,endPoint]) # x
    lines_to_plot.append([time, time]) # y
    lines_to_plot.append('k') # format
    #plt.plot([location,endPoint],[time,time], 'k')
  return lines_to_plot

#   plt.plot(*lines_to_plot)

# plt.xlabel("x"); plt.ylabel("y")
# plt.axis('equal')

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(*plotTPNG(0))
axs[0, 0].set_title('t=0')
axs[0, 1].plot(*plotTPNG(.4))
axs[0, 1].set_title('t=0.4')
axs[1, 0].plot(*plotTPNG(.8))
axs[1, 0].set_title('t=0.8')
axs[1, 1].plot(*plotTPNG(1))
axs[1, 1].set_title('t=1')

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')
    plt.xlabel("x"); plt.ylabel("y")
    plt.rcParams["figure.figsize"] = (20,20)
    ax.set_xlim(xMin, xMax)
    ax.set_ylim(yMin, yMax)
# plt.axis('equal')
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()

