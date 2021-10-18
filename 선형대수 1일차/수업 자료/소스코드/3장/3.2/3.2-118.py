import numpy as np
import matplotlib.pyplot as plt


# 벡터 [ 4 3 ] ^T
a = np.array([4, 3])


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


# 원점에서 시작하는 벡터 a를 그립니다.
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1)

# (0, -3)에서 시작하는 벡터 a를 그립니다.
ax.quiver(0, -3, a[0], a[1], angles='xy', scale_units='xy', scale=1)

# (1, 2)에서 시작하는 벡터 a를 그립니다.
ax.quiver(1, 2, a[0], a[1], angles='xy', scale_units='xy', scale=1)

# (-3, 1)에서 시작하는 벡터 a를 그립니다.
ax.quiver(-3, 1, a[0], a[1], angles='xy', scale_units='xy', scale=1)



start = -5
end = 10

ax.set_xticks(range(start, end))
ax.set_yticks(range(start, end))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')


ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
