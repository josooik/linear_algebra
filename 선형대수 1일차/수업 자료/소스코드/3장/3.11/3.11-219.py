import numpy as np
import matplotlib.pyplot as plt


A = np.array([[4, 3], [1, -2]])


# 고유벡터와 고유값 계산 
eigenvalue,eigenvector = np.linalg.eig(A)

eigenvector1 = eigenvector[:,0]
eigenvector2 = eigenvector[:,1]
lambda1 = eigenvalue[0]
lambda2 = eigenvalue[1]


# 1 x 3 크기의 서브 플롯 생성
f, ax= plt.subplots(1, 3)

# 서브 플롯 상단에 텍스트 추가
ax[0].title.set_text('v')
ax[1].title.set_text('Av')
ax[2].title.set_text('λv')

# Av, lambda*v 계산
s1 = np.dot(A, eigenvector1)
s2 = np.dot(A, eigenvector2)
w1 = np.dot(eigenvector1, lambda1)
w2 = np.dot(eigenvector2, lambda2)


# 벡터 표시
ax[0].quiver(0, 0, eigenvector1[0], eigenvector1[1], angles='xy', scale_units='xy', scale=1, color="black")
ax[0].quiver(0, 0, eigenvector2[0], eigenvector2[1], angles='xy', scale_units='xy', scale=1, color="black")
ax[0].text(eigenvector1[0], eigenvector1[1], 'v1', size=10)
ax[0].text(eigenvector2[0], eigenvector2[1], 'v2', size=10)
ax[1].quiver(0, 0, s1[0], s1[1], angles='xy', scale_units='xy', scale=1, color="red")
ax[1].quiver(0, 0, s2[0], s2[1], angles='xy', scale_units='xy', scale=1, color="red")
ax[1].text(s1[0], s1[1], 'Av1', size=10)
ax[1].text(s2[0], s2[1], 'Av2', size=10)
ax[2].quiver(0, 0, w1[0], w1[1], angles='xy', scale_units='xy', scale=1, color="blue")
ax[2].quiver(0, 0, w2[0], w2[1], angles='xy', scale_units='xy', scale=1, color="blue")
ax[2].text(w1[0], w1[1], '{:.2f}v1'.format(lambda1), size=10)
ax[2].text(w2[0], w2[1], ' {:.2f}v2'.format(lambda2), size=10)


# 그리드 생성
start_x = -1
end_x = 6
start_y = -3
end_y = 3
for i in range(3):
    ax[i].axis([start_x, end_x, start_y, end_y])
    ax[i].set_xticks(range(start_x, end_x))
    ax[i].set_yticks(range(start_y, end_y))
    ax[i].grid(True)
    ax[i].set_aspect('equal', adjustable='box')

plt.show()
