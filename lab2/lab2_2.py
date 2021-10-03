from timeit import default_timer as timer
import numpy as np

matrix_X = np.array([[12, 7, 3],
					[4 , 5, 6],
					[7 , 8, 9]])

matrix_Y = np.array([[5, 8, 1, 2],
					 [6, 7, 3, 0],
					 [4, 5, 9, 1]])
					 
vector_X = np.array([5, 6, 8])

vector_Y = np.array([1, 2, 3])

#matrix_X = np.random.random((500, 500))

#matrix_Y = np.random.random((500, 500))s

#vector_X = np.random.random((500))

#vector_Y = np.random.random((500))

					 
matrix_result = np.zeros((len(matrix_X), len(matrix_Y[0])))

vector_result_1 = np.zeros(len(vector_X))

vector_result_2 = np.zeros(len(vector_X))

number_result = 0


print('matrix X')
print(matrix_X)

print('\nmatrix Y')
print(matrix_Y)

print('\nvector X')
print(vector_X)

print('\nvector Y')
print(vector_Y)


print('\nmatrix x matrix')
start = timer()
matrix_result = matrix_X.dot(matrix_Y)
end = timer()
time_all = end - start

print(matrix_result)
print('time:', time_all)


print('\nmatrix x vector')
start = timer()
vector_result_1 = matrix_X.dot(vector_X)
end = timer()
time_all = end - start

print(vector_result_1)
print('time:', time_all)


print('\nvector x matrix')
start = timer()
vector_result_2 = vector_X.dot(matrix_X)
end = timer()
time_all = end - start

print(vector_result_2)
print('time:', time_all)


print('\nvector x vector')
start = timer()
number_result = vector_X.dot(vector_Y)
end = timer()
time_all = end - start

print(number_result)
print('time:', time_all)