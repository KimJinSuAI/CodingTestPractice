import numpy as np
import sympy as sym
from sympy.abc import x
from sympy.plotting import plot

train_x = np.array([[1,1,1], [1,1,2], [1,2,2], [2,2,3], [2,3,3], [1,2,3]])
train_y = np.dot(train_x, np.array([1,3,5])) + 7

# random initialize
beta_gd = [9.4, 10.6, -3.7, -1.2]
# for constant element
expand_x = np.array([np.append(x, [1]) for x in train_x])
lr_rate = 1e-2
for t in range(5000):
    error = train_y - expand_x @ beta_gd
    grad = -np.transpose(expand_x) @ error
    beta_gd = beta_gd - lr_rate*grad
    ## Todo


print("After gradient descent, beta_gd : {}".format(beta_gd))

