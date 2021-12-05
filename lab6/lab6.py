import numpy as np
import random
import os
import matplotlib.pyplot as plt

def function(x):
	result = 1.0 / (1 + np.exp(-x))
	return result

input = [[0, 0],
		 [0, 1],
		 [1, 0],
		 [1, 1]]
		 
output_and = [0, 0, 0, 1]

output_or = [0, 1, 1, 1]

iterations = 100

lr = 1
bias = 1

weights = list()
for k in range(3):
    weights.append(random.random())

def perceptron(input1, input2, output):
    outp_pn = input1 * weights[0] + input2 * weights[1] + bias * weights[2]
    outp_pn = function(outp_pn)
    err = output - outp_pn
    weights[0] += err * input1 * lr
    weights[1] += err * input2 * lr
    weights[2] += err * bias * lr

print("Number of iterations: ", iterations)


print("\nAND function")

for i in range(iterations):
	for x in range(len(output_and)):
		perceptron(input[x][0], input[x][1], output_and[x])
	
for pair in input:
	outp_pn = pair[0] * weights[0] + pair[1] * weights[1] + bias * weights[2]
	outp = function(outp_pn)
	print(pair[0], "AND", pair[1] ,"result:", outp)
	
k = -(weights[1] / weights[0]);
b = -(weights[2] / weights[0]);
x = np.linspace(-0.25, 1.25, 10)
y = k * x + b
plt.plot(x, y)
for pair in input:
	plt.scatter(pair[0], pair[1], c="red")
plt.title('AND function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

	
print("\nOR function")
		
for i in range(iterations):
	for x in range(len(output_or)):
		perceptron(input[x][0], input[x][1], output_or[x])
	
for pair in input:
	outp_pn = pair[0] * weights[0] + pair[1] * weights[1] + bias * weights[2]
	outp = function(outp_pn)
	print(pair[0], "OR", pair[1] ,"result:", outp)
	
k = -(weights[1] / weights[0]);
b = -(weights[2] / weights[0]);
x = np.linspace(-0.25, 1.25, 10)
y = k * x + b
plt.plot(x, y)
for pair in input:
	plt.scatter(pair[0], pair[1], c="red")
plt.title('AND function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


x = np.linspace(-5, 5, 100)
y = function(x)
plt.plot(x, y)
plt.grid()
plt.show()