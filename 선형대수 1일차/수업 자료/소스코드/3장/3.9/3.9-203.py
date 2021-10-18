import numpy as np
import matplotlib.pyplot as plt


# 행렬 A의 크기는 2 × 3
A = np.array([[1, 2, 3], [1, 5, 1]])

# 행렬 b의 크기는 2 × 1
b = np.array([2, 1])

x = np.linalg.lstsq(A, b, rcond=-1)[0]


a1 = A[:, 0]
a2 = A[:, 1]


sum = a1 * x[0] + a2 * x[1]


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


ax.quiver(0, 0, sum[0], sum[1], angles='xy', scale_units='xy', scale=1)
ax.text(sum[0], sum[1], "b_", size=20)
ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1)
ax.text(b[0], b[1], "b", size=20)



ax.set_xticks(range(0, 3))
ax.set_yticks(range(0, 3))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
