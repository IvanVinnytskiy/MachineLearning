from timeit import default_timer as timer
import unittest
import numpy as np

class MultiplyMethods:
	def multiply_matrix_matrix(matrix_A, matrix_B):
		matrix_result = [[0 for y in range(len(matrix_B[0]))]
				 for x in range(len(matrix_A))]
				 
		for i in range(len(matrix_A)):
			for j in range(len(matrix_B[0])):
				for k in range(len(matrix_B)):
					matrix_result[i][j] += matrix_A[i][k] * matrix_B[k][j]
					
		return 	matrix_result
	
	def multiply_matrix_vector(matrix, vector):
		vector_result = [0 for x in range(len(vector))]
		
		for i in range(len(matrix)):
			for j in range(len(vector)):
				vector_result[i] += matrix[i][j] * vector[j]
				
		return vector_result
		
	def multiply_vector_matrix(vector, matrix):
		vector_result = [0 for x in range(len(vector))]
		
		for i in range(len(vector)):
			for j in range(len(matrix)):
				vector_result[i] += vector[j] * matrix[j][i]
		
		return vector_result
		
	def multiply_vector_vector(vector_A, vector_B):
		number_result = 0
		
		for i in range(len(vector_A)):
			number_result += vector_A[i] * vector_B[i]
			
		return number_result
	
class TestMultiplyMethods(unittest.TestCase):

	def test_matrix_size_valid(self):
		matrix_A_test = [[1 for y in range(3)]
             for x in range(3)]
			 
		matrix_B_test = [[1 for y in range(4)]
             for x in range(3)]
			 
		matrix_result_test = MultiplyMethods.multiply_matrix_matrix(matrix_A_test, matrix_B_test)
		
		matrix_columns_A = len(matrix_A_test[0])
		matrix_rows_B = len(matrix_B_test)
	
		self.assertEqual(matrix_columns_A, matrix_rows_B)
		
	def test_matrix_size_invalid(self):
		matrix_A_test = [[1 for y in range(3)]
             for x in range(3)]
			 
		matrix_B_test = [[1 for y in range(4)]
             for x in range(4)]
		
		with self.assertRaises(IndexError):
			matrix_result_test = MultiplyMethods.multiply_matrix_matrix(matrix_A_test, matrix_B_test )

	def test_matrix_size_output_valid(self):
		matrix_A_test = [[1 for y in range(3)]
             for x in range(3)]
			 
		matrix_B_test = [[1 for y in range(4)]
             for x in range(3)]
			 
		matrix_result_test = MultiplyMethods.multiply_matrix_matrix(matrix_A_test, matrix_B_test)
		
		matrix_rows_should = len(matrix_A_test)
		matrix_columns_should = len(matrix_B_test[0])
		matrix_rows_exist = len(matrix_result_test)
		matrix_columns_exist = len(matrix_result_test[0])
	
		self.assertEqual(matrix_rows_exist, matrix_rows_should)
		self.assertEqual(matrix_columns_exist, matrix_columns_should)
		
	def test_matrix_matrix_multiply_valid(self):
		matrix_A_test = [[1, 2, 3],
						 [4, 5, 6],
						 [7, 8, 9]]
						 
		matrix_B_test = [[1, 2, 3],
						 [4, 5, 6],
						 [7, 8, 9]]
		
		matrix_result_should_test = [[30,  36,  42],
						             [66,  81,  96],
						             [102, 126, 150]]
			 
		matrix_result_exist_test = MultiplyMethods.multiply_matrix_matrix(matrix_A_test, matrix_B_test)
	
		self.assertEqual(matrix_result_exist_test, matrix_result_should_test)
		
	def test_matrix_vector_multiply_valid(self):
		matrix_test = [[1, 2, 3],
					   [4, 5, 6],
					   [7, 8, 9]]
			
		vector_test = [1, 2, 3]
		
		vector_result_should_test = [14, 32, 50]
		
		vector_result_exist_test = MultiplyMethods.multiply_matrix_vector(matrix_test, vector_test)
		
		self.assertEqual(vector_result_exist_test, vector_result_should_test)
		
	def test_vector_matrix_multiply_valid(self):
		vector_test = [1, 2, 3]
		
		matrix_test = [[1, 2, 3],
					   [4, 5, 6],
					   [7, 8, 9]]
		
		vector_result_should_test = [30, 36, 42]
		
		vector_result_exist_test = MultiplyMethods.multiply_vector_matrix(vector_test, matrix_test)
		
		self.assertEqual(vector_result_exist_test, vector_result_should_test)
		
	def test_vector_vector_multiply_valid(self):
		vector_A_test = [1, 2, 3]
			
		vector_B_test = [1, 2, 3]
		
		vector_result_should_test = 14
		
		vector_result_exist_test = MultiplyMethods.multiply_vector_vector(vector_A_test, vector_B_test)
		
		self.assertEqual(vector_result_exist_test, vector_result_should_test)
		
	

matrix_X = [[12, 7, 3],
			[4 , 5, 6],
			[7 , 8, 9]]

matrix_Y = [[5, 8, 1, 2],
			[6, 7, 3, 0],
			[4, 5, 9, 1]]
			
vector_X = [5, 6, 8]

vector_Y = [1, 2, 3]

#matrix_X = np.random.random((500, 500))

#matrix_Y = np.random.random((500, 500))

#vector_X = np.random.random((500))

#vector_Y = np.random.random((500))

print('matrix X')
for r in matrix_X:
   print(r)

print('\nmatrix Y')
for r in matrix_Y:
   print(r)

print('\nvector X')
print(vector_X)

print('\nvector Y')
print(vector_Y)

print('\nmatrix x matrix')
start = timer()				
matrix_result = MultiplyMethods.multiply_matrix_matrix(matrix_X, matrix_Y)
end = timer()
time_all = end - start

for r in matrix_result:
   print(r)
print('time:', time_all)
  
print('\nmatrix x vector')
start = timer()
vector_result_1 = MultiplyMethods.multiply_matrix_vector(matrix_X, vector_X)	
end = timer()
time_all = end - start

print(vector_result_1)
print('time:', time_all)

print('\nvector x matrix')
start = timer()
vector_result_2 = MultiplyMethods.multiply_vector_matrix(vector_X, matrix_X)
end = timer()
time_all = end - start

print(vector_result_2)
print('time:', time_all)

print('\nvector x vector')
start = timer()
number_result = MultiplyMethods.multiply_vector_vector(vector_X, vector_Y)
end = timer()
time_all = end - start
		
print(number_result)
print('time:', time_all)

unittest.main()