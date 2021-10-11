from timeit import default_timer as timer
import numpy as np

# дані для перевірки правильності обрахунків
matrix_X = np.array([[12, 7, 3],
					[4 , 5, 6],
					[7 , 8, 9]])

matrix_Y = np.array([[5, 8, 1, 2],
					 [6, 7, 3, 0],
					 [4, 5, 9, 1]])
					 
vector_X = np.array([5, 6, 8])

vector_Y = np.array([1, 2, 3])


# дані для вимірів часу
#matrix_X = np.random.random((500, 500))

#matrix_Y = np.random.random((500, 500))s

#vector_X = np.random.random((500))

#vector_Y = np.random.random((500))


# виведення початкових (вхідних) даних
print('matrix X')
print(matrix_X)

print('\nmatrix Y')
print(matrix_Y)

print('\nvector X')
print(vector_X)

print('\nvector Y')
print(vector_Y)


# множення матриці на матрицю
print('\nmatrix x matrix')
start = timer() # початок відліку часу
matrix_result = matrix_X.dot(matrix_Y) # метод бібліотеки NumPy
end = timer() # кінець відліку часу
time_all = end - start # обчислення часу виконання

print(matrix_result) # виведення результатів обрахунків
print('time:', time_all) # виведення часу виконання


# множення матриці на вектор
print('\nmatrix x vector')
start = timer()
vector_result_1 = matrix_X.dot(vector_X) # метод бібліотеки NumPy
end = timer()
time_all = end - start

print(vector_result_1)
print('time:', time_all)


# множення вектора на матрицю
print('\nvector x matrix')
start = timer()
vector_result_2 = vector_X.dot(matrix_X) # метод бібліотеки NumPy
end = timer()
time_all = end - start

print(vector_result_2)
print('time:', time_all)


# множення вектора на вектор
print('\nvector x vector')
start = timer()
number_result = vector_X.dot(vector_Y) # метод бібліотеки NumPy
end = timer()
time_all = end - start

print(number_result)
print('time:', time_all)
