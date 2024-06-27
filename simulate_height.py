from tPNG import simulate_height
import numpy as np
import matplotlib.pyplot as plt

'''Plot the normalized height function at (n, n) 
as a function of t, compare with the theoretical 
limit 2/\sqrt{1-t}'''   

n = 500
m = 100
x_val = np.linspace(0.05, 0.95, m+1)
y_val = np.empty(m+1)
for i in range(m+1):
    t = 0.05 + 0.9/m*i
    y_val[i] = simulate_height(t, n, n)/n
    if i % 10 == 0:
        print(f"Have execute {i} step")

fig, ax = plt.subplots(1, 1, figsize = (5, 5))
ax.plot(x_val, y_val, 'b')
ax.plot(np.linspace(0.05, 0.95, m+1), 2/np.sqrt(1-np.linspace(0.05, 0.95, m+1)), 'r')
plt.show()