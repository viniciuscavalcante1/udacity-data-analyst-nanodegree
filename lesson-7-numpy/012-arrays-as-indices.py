import numpy as np

x = np.arange(20).reshape(4, 5)
print(x)

indices = np.array([1, 3])
print(indices)

y = x[indices, :]
print(y)
