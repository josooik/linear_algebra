import numpy as np
import matplotlib.pyplot as plt


A = np.array([[2, 0], [0, 3]])


eigenvalue,eigenvector = np.linalg.eig(A)

eigenvector1 = eigenvector[:,0]
eigenvector2 = eigenvector[:,1]
lambda1 = eigenvalue[0]
lambda2 = eigenvalue[1]


f, ax= plt.subplots(1, 1)



v1 = np.dot(A, eigenvector1)
v2 = np.dot(A, eigenvector2)


  
for theta in range(0,360,10):  
    radian = theta*np.pi/180  
    X1=2*np.cos(radian)  
    Y1=2*np.sin(radian)  
    X2=4*np.cos(radian)
    Y2=4*np.sin(radian)

    U,V = np.dot(A, np.array([X2, Y2]))

    ax.quiver(X1, Y1, X2, Y2, angles='xy', scale_units='xy', scale=1, color='blue')
    ax.quiver(X1, Y1, U, V, angles='xy', scale_units='xy', scale=1, color='red')


ax.quiver(0, 0, eigenvector1[0]*eigenvalue[0], eigenvector1[1]*eigenvalue[0], angles='xy', scale_units='xy', scale=1, color='green')
ax.quiver(0, 0, eigenvector2[0]*eigenvalue[1], eigenvector2[1]*eigenvalue[1], angles='xy', scale_units='xy', scale=1, color='green')


start_x = -12
end_x = 12
start_y = -17
end_y = 17

ax.axis([start_x, end_x, start_y, end_y])
ax.set_xticks(range(start_x, end_x))
ax.set_yticks(range(start_y, end_y))
ax.grid(True)
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')


plt.show()
