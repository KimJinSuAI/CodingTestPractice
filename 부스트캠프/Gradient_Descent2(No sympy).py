import numpy as np
import sympy as sym
from sympy.abc import x
from sympy.plotting import plot

def func(val):
    fun = sym.poly(x**2 + 2*x + 3)
    return fun.subs(x, val)

def difference_quotient(f, x, h=1e-9):
    result = (f(x+h)-f(x))/h
    ## Todo

    return result

def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    diff = difference_quotient(fun, init_point)
    while np.abs(diff)>epsilon:
        val = val - lr_rate*diff
        diff = difference_quotient(fun, val)
        cnt+=1

    print("연산횟수: {}\n최소점: ({}, {})".format(cnt, val, func(val)))

gradient_descent(func,3)