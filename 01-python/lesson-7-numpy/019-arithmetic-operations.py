import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
print(x)
print(y)

print(x + y)
print(np.add(x, y))  # add

print(x - y)
print(np.subtract(x, y))
print(x * y)
print(np.multiply(x, y))
print(x / y)
print(np.divide(x, y))

# with two dimensional arrays
X = np.array([1, 2, 3, 4]).reshape(2, 2)
print(x)

Y = np.array([5, 6, 7, 8]).reshape(2, 2)
print(y)

print(X + Y)
print(X - Y)
print(X * Y)
print(Y / Y)

print(x)
print(np.sqrt(x))  # square root
print(np.exp(x))  # exponential
print(np.power(x, 2))  # power of 2

# statistical methods
print(X)
print("average: ", X.mean())
print("column average: ", X.mean(axis=0))
print("row average: ", X.mean(axis=1))
print("sum: ", X.sum())
print("sum of columns: ", X.sum(axis=0))
print("sum of rows: ", X.sum(axis=1))
print("std: ", X.std())
print("median: ", np.median(X))
print("max: ", X.max())
print("min: ", X.min())

# add to array
print(X)
print(X + 3)
print(X - 3)
print(X * 3)
print(X / 3)

# broadcasting

Y = np.arange(9).reshape(3, 3)
print(Y)

x = np.arange(3)
print(x)

print(Y + x)  # numpy broadcast, arange(3) adds every row to arange(9).reshape(3, 3) to produce
# compatible shapes
