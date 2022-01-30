import numpy as np

# create a matrix of zeros
zeros = np.zeros((3, 4), dtype=int)
print("Zeros matrix: ", zeros)

# create a matrix of ones
ones = np.ones((4, 5), dtype=int)
print("Ones matrix: ", ones)

# create a matrix of the desired number
full = np.full((4, 3), 7, dtype=int)
print("Full matrix: ", full)

# create an identity matrix (square shaped matrix that has ones along its main diagonal and zeros
# everywhere else)
eye = np.eye(3)
print("Eye/identity matrix: ", eye)

# create a diagonal matrix
diag = np.diag([10, 20, 30, 40])
print("Diag/diagonal matrixx: ", diag)

# create a bi-dimensional array with ordered values:
arange_one_parameter = np.arange(10)
print("arange with only one parameter, stop: ", arange_one_parameter)

arange_two_parameters = np.arange(4, 10)
print("arange with two parameters, start and stop: ", arange_two_parameters)

arange_three_parameters = np.arange(1, 14, 3)
print("arange with three parameters, start, stop and step: ", arange_three_parameters)

# create a bi-dimensional array with floating point numbers in step:
linspace = np.linspace(0, 25, 10)
print("linspace: ", linspace)

linspace_endpoint = np.linspace(0, 25, 10, endpoint=False)
print("linspace with endpoint: ", linspace_endpoint)

# convert a bi-dimensional array into a matrix:
one_dimensional = np.arange(20)
print("one dimensional array: ", one_dimensional)

matrix = np.reshape(one_dimensional, (4, 5))
print("matrix: ", matrix)

# the statement above with only one line of code:
matrix2 = np.arange(20).reshape((10, 2))
print("matrix in one line of code: ", matrix2)

# now, with the linspace function:
linspace_matrix = np.linspace(0, 50, 10, endpoint=False).reshape(5, 2)
print("matrix of linspace: ", linspace_matrix)

# random np matrix:
random_matrix = np.random.random((3, 3))
print("random matrix: ", random_matrix)

# random matrix with min and max numbers:
random_matrix_bounds = np.random.randint(4, 15, (3, 3))
print("random matrix with min and max numbers: ", random_matrix_bounds)

# random matrix with statistical purposes:
normal = np.random.normal(0, 0.1, size=(5, 5))
print("random matrix with normal distribution: ", normal)
