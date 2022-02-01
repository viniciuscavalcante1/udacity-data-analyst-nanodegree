import numpy as np

x = np.random.randint(1, 11, size=(10,))
print(x)

print(np.sort(np.unique(x)))  # doesn't affect original array

x.sort()  # this affects original array

y = np.random.randint(1, 11, size=(5, 5))
print(y)

print(np.sort(x, axis=0))  # axis 0 = rows
print(np.sort(x, axis=1))  # axis 1 = columns
