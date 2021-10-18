# 한 평면 위의 3개의 벡터
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 5, 0])
b = np.array([4, 4, 0])
c = np.array([4, 7, 0])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# 벡터 a를 그립니다.
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='black', arrow_length_ratio=0.1)
ax.text(a[0], a[1], a[2], 'a', size=15)

# 벡터 b를 그립니다.
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='black', arrow_length_ratio=0.1)
ax.text(b[0], b[1], b[2], 'b', size=15)

# 벡터 c를 그립니다.
ax.quiver(0, 0, 0, c[0], c[1], c[2], color='blue', arrow_length_ratio=0.1)
ax.text(c[0], c[1], c[2], 'c', size=15, color='blue')


ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=20., azim=35)
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('auto', adjustable='box')

plt.show()