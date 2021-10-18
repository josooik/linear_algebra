import numpy as np
import matplotlib.pylab as plt

fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


x = np.arange(-10, 10, 0.1)

# 가중치에 변화를 줍니다. 
W = np.arange(0.5, 3, 0.5)

for w in W:
	# 입력 x에 가중치 w를 곱합니다.
	f = 1 / (1 + np.exp(-x*w))
	ax.plot(x, f)

ax.set_xticks(range(-10, 10))
ax.set_yticks(range(0, 2))
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
plt.show()
