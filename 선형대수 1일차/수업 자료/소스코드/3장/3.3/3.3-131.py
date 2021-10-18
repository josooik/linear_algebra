import numpy as np
import matplotlib.pyplot as plt


a = np.array([4, 1])
c = -3
ca = np.multiply(c, a)


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


# 벡터 a를 그립니다.
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1)
plt.text(a[0], a[1], 'a', size=15)

# 벡터 a에 -3을 곱한 벡터를 그립니다. 시작점을 (4,0)으로 하여 그렸습니다.
plt.quiver(4, 0, ca[0], ca[1], angles='xy', scale_units='xy', scale=1, color='red')
plt.text(ca[0]+2.2, ca[1], '-3a', size=15, color='red')


ax.set_xticks(range(-10, 7))
ax.set_yticks(range(-5, 5))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


plt.show()
