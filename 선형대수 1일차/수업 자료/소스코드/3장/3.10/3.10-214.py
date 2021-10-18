import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


points = np.array([[1,1],[1,2],[2,2],[2,1]])
A = np.array([[2, 0], [0, 2]])


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


print(np.linalg.det(A))


ax.add_patch(patches.Polygon(points, fill=False, color='blue', zorder=1))
ax.add_patch(patches.Polygon(np.dot(points,A), fill=False, color="red", zorder=2))
ax.text(1.4, 1.4, 'A', size=15)
ax.text(2.9, 2.9, 'B', size=15)


ax.set_xticks(range(-1, 6))
ax.set_yticks(range(-1, 6))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')


ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
