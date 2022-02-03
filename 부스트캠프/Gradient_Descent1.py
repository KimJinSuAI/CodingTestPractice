import numpy as np
import sympy as sym
from sympy.abc import x
from sympy.plotting import plot

def func(val):
    fun = sym.poly(x**2 + 2*x + 3)
    return fun.subs(x, val), fun

def func_gradient(fun, val):
    ## TODO
    v,p = fun(val)
    diff = sym.diff(sym.poly(p))
    return diff.subs(x, val), diff

def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    diff, _ = func_gradient(fun, init_point)
    while np.abs(diff)>epsilon:
        val = val - lr_rate*diff
        diff, _ = func_gradient(fun, val)
        cnt+=1
    ## Todo
    
    print("함수: {}\n연산횟수: {}\n최소점: ({}, {})".format(fun(val)[1], cnt, val, fun(val)[0]))

gradient_descent(func,3)