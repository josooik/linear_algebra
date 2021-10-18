import numpy as np
import matplotlib.pyplot as plt


a = np.array([4, 1])
c = 3
ca = np.multiply(c, a)


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


# 벡터 a를 그립니다.
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1)
plt.text(a[0], a[1], 'a', size=15)

# 벡터 a에 3을 곱한 결과를 그립니다. 시작점을 (0,1)로 이동하여 그렸습니다. 
plt.quiver(0, 1, ca[0], ca[1], angles='xy', scale_units='xy', scale=1, color='blue')
plt.text(ca[0], ca[1]+1, '3a', size=15, color='blue')


ax.set_xticks(range(-2, 15))
ax.set_yticks(range(-3, 9))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')


ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


plt.show()
