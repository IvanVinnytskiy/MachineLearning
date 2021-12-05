from math import *
import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt

iterations = 100

def function(x):
    return x ** 2

def derivative_my(f, x, eps):
    return (f(x + eps) - f(x)) / eps

def grad(x0, alpha, eps, f):
    x = [x0]
    i = 0
    while i < iterations:
        i += 1
        xNew = x[-1] - alpha * derivative_my(f, x[-1], 1e-6)
        x.append(xNew)
        if abs(x[-1] - x[-2]) < eps:
            break
    return x[:-1], x[-1]
	
func_vectorize = np.vectorize(function)

x_data = np.arange(-4, 4, 0.01)
y_data = func_vectorize(x_data)

gradient_points, gradient_minimum = grad(3, 0.1, 0.0001, function)

print("Gradient descent points:")
print(gradient_points)
print("\nNumber of iterations:")
print(len(gradient_points))
print("\nMinimum:")
print(gradient_minimum)

der = derivative(function, 5, dx=1e-6)
der_my = derivative_my(function, 5, 1e-6)
eps = abs(der - der_my)
print("\nDerivative: ", der)
print("My derivate: ", der_my)
print("Eps: ", eps)

plt.plot(x_data, y_data, label='Function')
plt.scatter(gradient_points, func_vectorize(gradient_points), color="red", label='Gradient descent')
plt.scatter(gradient_minimum, function(gradient_minimum), color='green', label='Minimum')
plt.legend(loc="upper left")
plt.show()