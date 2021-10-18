import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1, 1], [2, 2]])
b = np.array([10, 20])


a1 = A[:, 0]
a2 = A[:, 1]


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


# a1과 a2에 의해 만들어지는 생성(span)을 그림 
line_x = []
line_y = []

for c1 in np.linspace(-5, 25, 25):
    for c2 in np.linspace(-5, 25, 25):
        c1_a1 = a1*c1
        c2_a2 = a1*c2
        sum = c1_a1 + c2_a2
        line_x.append(sum[0])
        line_y.append(sum[1])

ax.plot(line_x, line_y, color="red", zorder=1)


# 벡터 a1, a2, b를 그림
ax.quiver(0, 0, a1[0], a1[1], angles='xy', scale_units='xy', scale=1, zorder=3)
ax.quiver(0, 0, a2[0], a2[1], angles='xy', scale_units='xy', scale=1, zorder=3)
ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color="blue", zorder=2)
ax.text(a1[0]+0.5, a1[1], "a1=a2", size=15)
ax.text(b[0], b[1], "b", size=15)



ax.axis([-3, 12, -3, 22])
ax.set_xticks(range(-3, 12))
ax.set_yticks(range(-3, 22))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
