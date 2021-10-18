import numpy as np
import matplotlib.pyplot as plt


A = np.array([[2, 0], [0, 3]])


eigenvalue,eigenvector = np.linalg.eig(A)

eigenvector1 = eigenvector[:,0]
eigenvector2 = eigenvector[:,1]
lambda1 = eigenvalue[0]
lambda2 = eigenvalue[1]


f, ax= plt.subplots(1, 2)


points = np.array([[-1, 1,], [1, 1,], [1, -1,], [-1, -1,], [-1, 1,]])
x = points[:, 0]
y = points[:, 1]



for idx in range(len(points)-1):

    ax[0].plot([points[idx,0], points[idx+1,0]], [points[idx,1], points[idx+1,1]], color='black' )

    new_point1 = np.dot(A, points[idx])
    new_point2 = np.dot(A, points[idx+1])
    ax[1].plot([new_point1[0], new_point2[0]], [new_point1[1], new_point2[1]], color='black' )


v1 = np.dot(A, eigenvector1)
v2 = np.dot(A, eigenvector2)

w = np.array([1, 1])
w_ = np.dot(A, w)


ax[0].quiver(0, 0, eigenvector1[0], eigenvector1[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.01)
ax[0].quiver(0, 0, eigenvector2[0], eigenvector2[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.01)
ax[0].quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.01)
ax[0].text(eigenvector1[0]+0.5, eigenvector1[1], 'v1', size=15)
ax[0].text(eigenvector2[0], eigenvector2[1]+0.5, 'v2', size=15)
ax[0].text(w[0], w[1], 'w', size=15)
ax[1].quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color="blue", width=0.01)
ax[1].quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color="blue", width=0.01)
ax[1].quiver(0, 0, w_[0], w_[1], angles='xy', scale_units='xy', scale=1, color="red", width=0.01)
ax[1].text(v1[0]+0.5, v1[1], 'v1', size=15)
ax[1].text(v2[0], v2[1]+0.5, 'v2', size=15)
ax[1].text(w_[0], w_[1]+0.5, 'w', size=15)


start_x = -5
end_x = 5
start_y = -6
end_y = 6

for i in range(2):
    ax[i].axis([start_x, end_x, start_y, end_y])
    ax[i].set_xticks(range(start_x, end_x))
    ax[i].set_yticks(range(start_y, end_y))
    ax[i].grid(True)
    ax[i].set_axisbelow(True)
    ax[i].set_aspect('equal', adjustable='box')


plt.show()
