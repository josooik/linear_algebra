# 내적 : 대응하는 성분끼리 곱해서 모두 더하는 것
import numpy as np

a = np.array([1, 2])

b = np.array([2, 3])

print(np.dot(a, b))

print()

a = np.array([1, 2])

print(np.linalg.norm(a))

print()

# norm 함수의 계산 결과는 제곱근 5와 같습니다.
print(np.sqrt(5))

print()

a = np.array([1, 2])

print(np.dot(a, a))

print()

# 자기 자신의 대한 내적의 제곱근
print(np.sqrt(np.dot(a, a)))

print()

# 벡터킈 크기
print(np.linalg.norm(a))

print()

a = np.array([3, 3])
b = np.array([3, 0])

print(np.dot(a, b))

print()

norm_a = np.linalg.norm(a)
print(norm_a)

print()

norm_b = np.linalg.norm(b)
print(norm_b)

print()

print(norm_a * norm_b * np.cos(45 * np.pi / 180))

print()

# 내적이 0이면 두벡터가 이루는 각도는 90도입니다.

a = np.array([3, 0])
b = np.array([0, 3])

print(np.dot(a, b))