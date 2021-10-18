import numpy as np
import matplotlib.pylab as plt

fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)

x = np.arange(-10, 10, 0.1)
f = 1 / (1 + np.exp(-x))

ax.plot(x, f)
ax.set_xticks(range(-10, 10))
ax.set_yticks(range(0, 2))
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
plt.show() 
