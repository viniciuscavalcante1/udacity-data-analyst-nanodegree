import numpy as np

x = np.array([1, 2, 5, 6, 7])
print(x)

x = np.insert(x, 2, [3, 4])
print(x)

y = np.array([[1, 2, 3], [7, 8, 9]])
print(y)

w = np.insert(y, 1, [4, 5, 6], axis=0)

v = np.insert(y, 1, 5, axis=1)
print(v)
