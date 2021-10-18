import matplotlib.pyplot as plt
import numpy as np


# 최소값을 구할 2차 함수 
def f(x):
    return np.power(x-5, 2) - 20


# 주어진 2차 함수의 1차 도함수
def f_derivative(x):
    return 2*x - 10


# 경사 하강법 구현한 함수 
def gradient_descent(next_x, gamma, precision, max_iteration):

    # 반복할 때마다 이동한 거리의 변화 추이를 살펴보기 위해 리스트에 저장합니다.
    list_step = []


    # 주어진 함수의 최소값을 찾기 위해 최대  max_iteration만큼 반복합니다.
    for i in range(max_iteration):
        
# 현재 위치에서 현재 위치에서의 기울기를 빼서 위치를 업데이트합니다. 
# 계산된 위치는 다음 번 반복시 현재 위치로 사용됩니다. 
        current_x = next_x
        next_x = current_x - gamma*f_derivative(current_x)


        # 현재 위치에서 다음 위치까지 이동하는 거리(x좌표 기준)를 측정하여 리스트에 저장합니다. 
        step = next_x - current_x
        list_step.append(abs(step))

        # 50번 반복할 때 마다 로그를 출력합니다. 
        if i%50==0:
            print('{}/{}, x={:5.6f}, f(x)={:5.6f}, gradient = {:5.6f}, gradient sign= {}'.format(i, max_iteration, current_x, f(current_x), gamma*f_derivative(current_x), '+' if f_derivative(current_x) > 0 else '-'))

        # 지정한 값보다 이동한 거리가 작아지면 루프를 중지합니다. 
        if abs(step) <= precision:
            break

    # 최종적으로 구한 최소값 위치에 있는 x 좌표입니다. 
    print('함수의 최소값은 x= {}일 때 입니다.'.format(current_x))


    # 이동거리의 변화 추이를 그래프로 그립니다. 
    Figure, ax= plt.subplots(1, 1)

    ax.title.set_text('step size')
    ax.plot(list_step)
    ax.set_ylabel('step size')
    ax.set_xlabel('Iteration number')

    plt.show()


# 시작 위치가 음수인 경우 경사하강법을 수행합니다.
gradient_descent(next_x=-10, gamma=0.01, precision=0.00001, max_iteration=1000)

# 시작 위치가 양수인 경우 경사하강법을 수행합니다.
gradient_descent(next_x=10, gamma=0.01, precision=0.00001, max_iteration=1000)
