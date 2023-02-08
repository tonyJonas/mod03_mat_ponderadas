
import math
x1 = 0.5

def f(x):
    return x-math.cos(x)**2

def df(x):
    return 1+2*math.sin(x)*math.cos(x)

def newton(x):
    return x - f(x)/df(x)

def erro(x, xk_antigo):
    return abs(x - xk_antigo)/abs(x)

xk = x1
xk_antigo = 0

for i in range(4):
    k = i
    fxk = f(xk)
    dfxk = df(xk)
    error = erro(xk, xk_antigo)
    print(f"k = {k} | xk = {xk} | f(xk) = {fxk} | df(xk) = {dfxk} | erro = {error}\n")
    xk_antigo = xk
    xk = newton(xk)