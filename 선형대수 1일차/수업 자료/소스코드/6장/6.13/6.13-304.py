import numpy as np
import matplotlib.pyplot as plt


# 활성화 함수로 시그모이드 함수를 사용합니다.
def sigmoid(x):  
    return 1 / (1 + np.exp(-x))

# 역전파 알고리즘 사용시 활성화 함수의 1차 도함수가 필요합니다. 
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# 피드포워드를 수행합니다. 
def feed_forward(x, W1, W2, b1, b2):
    a1 = x
    
    z2 = np.dot(W1, a1) + b1
    a2 = sigmoid(z2)

    z3 = np.dot(W2, a2) + b2
    a3 = sigmoid(z3)

    return a1, a2, a3, z2, z3


# 신경망은 총 3개의 레이어로 구성되며
# 입력 레이어의 노드 개수 3, 히든 레이어의 레이어 개수 3, 출력 레이어의 개수 1입니다. 
node_size = {
    'input_layer_size' : 3,
    'hidden_layer_size' : 3,
    'output_layer_size' : 1
}

# 학습률은 2.0입니다. 
learning_rate = 2.0


# 초기 가중치 값으로 무작위 값을 사용합니다. 
W2 = np.random.random((node_size['output_layer_size'], node_size['hidden_layer_size']))
W1 = np.random.random((node_size['hidden_layer_size'], node_size['input_layer_size']))
b2 = np.random.random(node_size['output_layer_size'])
b1 = np.random.random(node_size['hidden_layer_size'])


# 학습 데이터 세트입니다. 
# 특성 X, 라벨 Y
X = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0], [1, 1, 1]])
Y = np.array([1, 0, 0, 0, 1, 1, 0])


# 반복 횟수를 카운트하기 위해 사용합니다.
count = 0

# 학습 데이터 세트 전체에 대한 피드포워드와 역전파를 1000번 반복합니다.
max_iteration = 1000

# 학습 데이터 세트에 포함된 데이터의 개수입니다. 
dataset_size = len(Y)

# 반복할때마다 변하는 비용을 저장하기 위한 리스트입니다.
list_average_cost = []


# 정해놓은 max_iteration만큼 반복합니다.
while count < max_iteration:

    # 역전파 알고리즘 적용시 각 샘플별로 측정되는 값을 저장하기 위해 사용됩니다.  
    dW2 = np.zeros((node_size['output_layer_size'], node_size['hidden_layer_size']))
    dW1 = np.zeros((node_size['hidden_layer_size'], node_size['input_layer_size']))
    db2 = np.zeros((node_size['output_layer_size']))
    db1 = np.zeros((node_size['hidden_layer_size']))

    average_cost = 0

    # 학습 데이터 세트의 모든 샘플을 대상으로 
    # 피드포워드와 역전파 알고리즘을 수행합니다.  
    for x,y in zip(X,Y):

        # 피드포워드를 실행합니다. 
        a1,a2,a3,z2,z3 = feed_forward(x, W1, W2, b1, b2)

        # 역전파 알고리즘을 실행합니다.
        delta3 = -(y - a3) * sigmoid_derivative(z3)
        average_cost += np.linalg.norm((y-a3), 2)/dataset_size

        delta2 = np.dot(W2.T, delta3) * sigmoid_derivative(z2)

        dW2 += np.dot(delta3[:,np.newaxis], np.transpose(a2[:,np.newaxis]))/dataset_size
        db2 += delta3/dataset_size

        dW1 += np.dot(delta2[:,np.newaxis], np.transpose(a1[:,np.newaxis]))/dataset_size
        db1 += delta2/dataset_size


    # 역전파 알고리즘 실행 결과를 사용하여 신경망의 가중치와 편향을 업데이트합니다. 
    W2 += -learning_rate * dW2 
    b2 += -learning_rate * db2 
    W1 += -learning_rate * dW1 
    b1 += -learning_rate * db1 

    # 매 반복마다 측정된 비용을 리스트에 저장합니다. 
    list_average_cost.append(average_cost)

    # 100번 반복시마다 비용을 출력합니다. 실행시 비용이 감소하는 추이를 보는데 사용합니다.
    if count % 100 == 0:
        print('{}/{}  cost : {}'.format(count, max_iteration, average_cost))

    count += 1


# 반복횟수에 대비 비용 그래프를 그립니다. 
Figure, ax= plt.subplots(1, 1)

ax.title.set_text('Average cost')

ax.plot(list_average_cost)

ax.set_ylabel('Average cost')
ax.set_xlabel('Iteration number')

plt.show()


# 간단하게 하기위해 테스트 데이터세트를 따로 사용하지 않고 
# 학습 데이터 세트를 가지고 피드포워드를 수행하여 
# 학습결과 네트워크 출력과 라벨을 비교해봅니다.   
for x,y in zip(X,Y):

    # 피드 포워드를 실행합니다. 
    a1,a2,a3,z2,z3 = feed_forward(x, W1, W2, b1, b2)
    print(y)
    print(a3)
