import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


A = np.array([[0, 1], [-2, 1], [2, 1]])
b = np.array([-1, -4, 8])
x = np.linalg.lstsq(A, b, rcond=-1)[0]


a1 = A[:, 0]
a2 = A[:, 1]


sum = a1 * x[0] + a2 * x[1]


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1, projection='3d')


ax.quiver(0, 0, 0, sum[0], sum[1], sum[2], color='red', arrow_length_ratio=0.1)
ax.text(sum[0], sum[1], sum[2], "b_", size=20)
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='blue', arrow_length_ratio=0.1)
ax.text(b[0], b[1], b[2], "b", size=20)



ax.set_xlim(-3, 8)
ax.set_ylim(-5, 8)
ax.set_zlim(0, 8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=20., azim=5)


plt.show()
