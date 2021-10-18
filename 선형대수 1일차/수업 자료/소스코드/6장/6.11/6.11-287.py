import numpy as np


# 활성화 함수
def sigmoid(x):  
    return 1 / (1 + np.exp(-x))


# 피드포워드 수행하는 함수
def feed_forward(x, W1, W2, b1, b2):

    # 입력 레이어
    a1 = x
    
    # 히든 레이어
    z2 = np.dot(W1, a1) + b1
    a2 = sigmoid(z2)

    # 출력 레이어
    # a3에 신경망의 출력이 저장됩니다. 
    z3 = np.dot(W2, a2) + b2
    a3 = sigmoid(z3)

    return a1, a2, a3, z2, z3


# 신경망을 구성하는 레이어의 노드 개수 지정
node_size = {
    'input_layer_size' : 3,
    'hidden_layer_size' : 3,
    'output_layer_size' : 1
}


# 가중치와 편향을 무작위 값으로 초기화하여 생성합니다. 
W2 = np.random.random((node_size['output_layer_size'], node_size['hidden_layer_size']))
W1 = np.random.random((node_size['hidden_layer_size'], node_size['input_layer_size']))
b2 = np.random.random(node_size['output_layer_size'])
b1 = np.random.random(node_size['hidden_layer_size'])


# 학습 데이터 세트입니다. 
# 특성 X, 라벨 Y
X = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0], [1, 1, 1]])
Y = np.array([1, 0, 0, 0, 1, 1, 0])


# 특성 하나인 x에 대해 피드포워드를 수행합니다.
# 라벨 하나인 y는 비용 계산을 위해 사용합니다. 
for x,y in zip(X,Y):
 
       # 특성과 가중치를 사용하여 피드포워드를 수행하고 
       # 결과를 리턴받습니다. 
       # 6.13장 에서 살펴볼 역전파 알고리즘에서 사용됩니다. 
	a1,a2,a3,z2,z3 = feed_forward(x, W1, W2, b1, b2)

# 신경망의 출력 a3와 라벨 y로부터 비용을 계산합니다. 
# L2 Norm 계산을 위해 넘파이에서 제공하는 함수를 사용합니다. 
	print('a3={}, y={}, Error(L2 Norm)={}'.format(a3, y, np.linalg.norm((y-a3), 2)))
