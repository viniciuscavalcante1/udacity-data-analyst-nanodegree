import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x)

x = np.delete(x, [0, 4])  # ndarray, list of indices
print(x)

y = np.arange(1, 10).reshape(3, 3)
print(y)

w = np.delete(y, 0, axis=0)  # ndarray, list of indices, axis
print(w)

v = np.delete(y, [0, 2], axis=1)  # ndarray, list of indices, axis
print(v)
