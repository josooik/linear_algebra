# 두 벡터가 평행하면 외적은 0입니다.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([3, 3, 0])
b = np.array([6, 6, 0])

print(np.cross(a, b))

print()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# 벡터 a를 그립니다.
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='black', arrow_length_ratio=0.1)
ax.text(a[0], a[1], a[2], 'a', size=15)

# 벡터 b를 그립니다.
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='black', arrow_length_ratio=0.1)
ax.text(b[0], b[1], b[2], 'b', size=15)

ax.set_xlim(0, 7)
ax.set_ylim(0, 7)
ax.set_zlim(0, 7)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=20., azim=35)
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('auto', adjustable='box')

plt.show()