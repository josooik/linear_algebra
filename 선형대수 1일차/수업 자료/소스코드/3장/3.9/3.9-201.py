import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 행렬 A의 크기는 2 × 3
A = np.array([[1, 2, 3], [1, 5, 1]])
# 행렬 b의 크기는 2 × 1
b_ = np.array([2, 1])

x = np.linalg.lstsq(A, b_, rcond=-1)[0]


fig = plt.figure()
ax = fig.gca(projection='3d')


dim = 10


a1 = A[0]
a2 = A[1]


a = a1[0]
b = a1[1]
c = a1[2]
d = -b_[0]

X1, Y1 = np.meshgrid([-dim, dim], [-dim, dim])
# aX1 + bY1 + cZ1 = d
# cZ1 = d - aX1 - bY1
# Z1 = (d - aX1 - bY1) / c
Z1 = (d - a*X1 - b*Y1) / c


a = a2[0]
b = a2[1]
c = a2[2]
d = -b_[1]
X2, Y2 = np.meshgrid([-dim, dim], [-dim, dim])
Z2 = (d - a*X2 - b*Y2) / c


v = np.cross(a1, a2)

for t in np.linspace(-1, 1, 10):
    x1 = x[0] + v[0] * t
    y1 = x[1] + v[1] * t
    z1 = x[2] + v[2] * t
    ax.scatter(x1, y1, z1, color='blue', zorder = 4)

ax.plot_surface(X1, Y1, Z1, color='red', alpha=.3, linewidth=0, zorder=1)
ax.plot_surface(X2, Y2, Z2, color='blue', alpha=.3, linewidth=0, zorder=3)

ax.scatter(x[0], x[1], x[2], color='red', zorder=5)


plt.show()
