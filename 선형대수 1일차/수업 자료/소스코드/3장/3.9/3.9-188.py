import numpy as np
import matplotlib.pyplot as plt


a1 = np.array([7, -7])
a2 = np.array([2, 5])
b = np.array([-5, 12])

# 연립 방정식의 계수 벡터 A를 구합니다.
A = np.column_stack((a1, a2))
# solve 함수로 해를 구합니다. 
x = np.linalg.solve(A, b)

# 벡터에 해벡터의  스칼라를 곱합니다.
x1, y1 = x
a1 = a1 * x1
a2 = a2 * y1


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


# 벡터 a1과 a2로 벡터b를 만들 수 있음을 확인합니다.  
ax.quiver(0, 0, a1[0], a1[1], angles='xy', scale_units='xy', scale=1)
ax.text(a1[0]-1, a1[1], 'a1', size=15)
ax.quiver(a1[0], a1[1], a2[0], a2[1], angles='xy', scale_units='xy', scale=1)
ax.text(a1[0]+a2[0]-1.5, a1[1]+a2[1], 'a2', size=15)
ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='blue')
ax.text(b[0], b[1], 'b', size=15, color='blue')



ax.set_xticks(range(-10, 5))
ax.set_yticks(range(-3, 15))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
