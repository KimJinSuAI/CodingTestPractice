import numpy as np
import sympy as sym
from sympy.abc import x
from sympy.plotting import plot

train_x = (np.random.rand(1000) - 0.5) * 10 #x 랜덤값
train_y = np.zeros_like(train_x)

def func(val):
    fun = sym.poly(7*x + 2)
    return fun.subs(x, val)

for i in range(1000):
    train_y[i] = func(train_x[i])           #y값...

# initialize
w, b = 0, 0

lr_rate = 1e-2                              #람다..
n_data = len(train_x)
errors = []

for i in range(100):                        #학습횟수 100번
    ## Todo
    # 예측값 y
    _y = w*train_x+b

    # L2 norm과 np_sum 함수 활용해서 error 정의
    error = abs(train_y-_y)
    # Error graph 출력하기 위한 부분
    errors.append(sum(error)/1000)

    # gradient
    gradient_w = -(2/n_data)*sum((train_y-_y)*train_x)
    gradient_b = -(2/n_data)*sum(train_y-_y)

    # w, b update with gradient and learning rate
    w = w - lr_rate * gradient_w
    b = b - lr_rate * gradient_b


print("w : {} / b : {} / error : {} ".format(w, b, errors[-1]))
from IPython.display import clear_output
import matplotlib.pyplot as plt

def plot(errors):
    clear_output(True)
    plt.figure(figsize=(20,5))
    plt.ylabel('error')
    plt.xlabel('time step')
    plt.plot(errors)
    plt.show()
plot(errors)