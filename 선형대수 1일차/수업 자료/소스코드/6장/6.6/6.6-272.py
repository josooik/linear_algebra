import numpy as np
import matplotlib.pylab as plt

fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


x = np.arange(-10, 10, 0.1)

# 가중치는 고정시키고
w = 0.5

# 편향에 변화를 줍니다. 
B = np.arange(-2, 2, 0.5)

for b in B:
       # 입력 x에 가중치 w를 곱한 후 편향 b를 더합니다.
	f = 1 / (1 + np.exp(-(x*w+b)))
	ax.plot(x, f)


ax.set_xticks(range(-10, 10))
ax.set_yticks(range(0, 2))
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
plt.show()
