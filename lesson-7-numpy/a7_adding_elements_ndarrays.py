import numpy as np

# rank one array
x = np.array([1, 2, 3, 4, 5])
print(x)

x = np.append(x, 6)
print(x)

x = np.append(x, [7, 8])

# rank two array
y = np.arange(1, 10).reshape(3, 3)
print(y)

w = np.append(y, [[10, 11, 12]], axis=0)
print(w)

v = np.append(y, [[10], [11], [12]], axis=1)
print(v)
