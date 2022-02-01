import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 2, 8, 4])

print(np.intersect1d(x, y))
print(np.setdiff1d(x, y))
print(np.union1d(x, y))
