import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x)

print("1st element: ", x[0])
print("1st element: ", x[-5])

# modifying:
x[3] = 20
print(x)

x = np.arange(1, 10).reshape(3, 3)
print(x)

print("Element at (0, 0): ", x[0, 0])
print("Element at (0, 1): ", x[0, 1])
print("Element at (2, 2): ", x[2, 2])

x[0, 0] = 20
print("Element at (0, 0): ", x[0, 0])
