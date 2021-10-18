import numpy as np
import matplotlib.pyplot as plt

# 벡터 [4 3]^T
a = np.array([4, 3])


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)

# 벡터를 화살표로 나타냅니다.
# 시작점은 원점, 끝점은 벡터 [4 3]^T 입니다. 
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1)
ax.text(a[0], a[1], 'a', size=15)


ax.set_xticks(range(0, 7))
ax.set_yticks(range(0, 7))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
