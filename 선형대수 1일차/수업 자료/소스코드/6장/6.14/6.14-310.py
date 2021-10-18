import numpy as np
import csv


# 숫자로 주어지는 y값을 길이 vector_length인 one-hot 벡터로 변환합니다.
def convert_y_to_one_hot_vector(y, vector_length):

    y_vect = np.zeros((len(y), vector_length))
    
    for i in range(len(y)):
        y_vect[i, y[i]] = 1
    
    return y_vect


# 붓꽃 품종을 딕셔너리로 정의하여 문자열로된 라벨을 숫자값 라벨로 변환하는데 사용합니다.
Species_Dict ={'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2} 


# 특성(X)와 라벨(Y)를 저장하는데 사용합니다.
X = []
Y = []

# csv 파일을 열어서 한줄씩 가져옵니다.
with open('Iris.csv', newline='') as file:
    reader = csv.reader(file)
    try:
        for i,row in enumerate(reader):
            if i > 0:
# csv로부터 읽어온 데이터를 특성과 라벨로 나누어 리스트에 저장합니다.
                X.append(np.array(row[1:5], dtype="float64"))
# 앞에서 정의한 딕셔너리를 이용하여 문자열 라벨을 숫자 라벨로 변환합니다.
                Y.append(Species_Dict[row[-1]])

        # 데이터가 저장된 리스트를 넘파이 배열로 변환합니다.
        X = np.array(X)
        Y = np.array(Y)

    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

# {0, 1, 2} 값을 가지는 라벨을 one-hot 인코딩을하여 {0 0 1, 0 1 0, 1 0 0}로 변환합니다. 
Y = convert_y_to_one_hot_vector(Y, vector_length=3)


# 데이터 셋을 무작위로 섞습니다. 
s = np.arange(Y.shape[0])
np.random.seed(0)
np.random.shuffle(s)

Y = Y[s]
X = X[s]
    

# 학습용 데이터(X_train,Y_train)와 테스트용 데이터(X_test,Y_test)를 8:2 비율로 사용합니다. 
size = len(Y)
p = int(size * 0.8)


X_train = X[0:p]
Y_train = Y[0:p]
X_test = X[p:]
Y_test = Y[p:]


# 학습용 데이터를 시험 삼아 출력해봅니다.
print(X_train[0])
print(Y_train[0])
