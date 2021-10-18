# 행렬의 정의
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)

print()

B = np.matrix([[1, 2, 3], [4, 5, 6]])
print(B)

print()

print(A.shape)

print()

print(B.shape)

print()

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2], [3, 4]])
C = np.array([[1, 2], [3, 4]])

print(A == B)

print()

print(A == C)

print()

print(A == B)

print()

print(A == C)

print()

# 행렬을 구상하는 열벡터와 행벡터를 구하는 방법
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# 행렬 A를 구성하는 행벡터를 출력합니다.
print(A[0])

print()

print(A[0, :])

print()

print(A[1])

print()

print(A[1, :])

print()

# 행렬 A를 구성하는 열벡터를 출력합니다.
print(A[:,0])

print()

print(A[:,1])

print()

print(A[:,2])

print()

print(A[:,3])

print()

# 행렬의 기본 연산
# 덧셈
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 1], [5, 2]])

print(A + B)

print()

print(np.add(A, B))

print()

# 뺼셈
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 1], [5, 2]])

print(A - B)

print()

print(np.subtract(A, B))

print()

# 스칼라곱
A = np.arange(9).reshape(3, 3)
print(A)

print()

c = 10

np.multiply(c, A)

print(c * A)

print()

# 곱셈

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[4, 1], [5, 2], [1, 2]])

print(A)

print()

print(B)

print()

print(A.dot(B))

print()

print(np.dot(A, B))

print()

A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 1], [5, 2]])

print(A * B)

print()

print(np.multiply(A, B))

print()

# 전치
X = np.array([[1, 2], [3, 4], [5, 6]])

print(X)

print()

print(X.T)

print()

print(np.transpose(X))

print()

# 항등 행렬과 역행렬
I = np.eye(3)

print(I)

print()

A = np.arange(9).reshape(3, 3)

print(A)

print()

print(np.dot(A, I) == A)

print()

print(np.dot(I, A) == A)

print()

A = np.array([[1, 2], [3, 4]])

# inv 함수를 사용하여 행렬 A의역 행렬을 구합니다.
invA = np.linalg.inv(A)

print(invA)

print()

print(np.dot(A, invA))

print()

# round() 함수를 사용하면 항등 행렬로 보입니다.
print(np.round(np.dot(A, invA)))

print()

print(np.round(np.dot(invA, A)))


