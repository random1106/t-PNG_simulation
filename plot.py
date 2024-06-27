import numpy as np
import matplotlib.pyplot as plt
import bisect
from tPNG import plot

xmin = 0
xmax = 12
ymin = 0
ymax = 12
t = 0.5

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.plot(*plot(t, xmax, ymax))
ax.set(xlabel='x', ylabel='y')
plt.xlabel("x"); plt.ylabel("y")
plt.rcParams["figure.figsize"] = (20,20)
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
plt.show()