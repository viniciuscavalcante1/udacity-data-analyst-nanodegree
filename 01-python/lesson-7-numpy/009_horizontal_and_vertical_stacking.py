import numpy as np

x = np.array([1, 2])
print("rank one ndarray x [1, 2]: ")
print(x)
print("---")

y = np.array([[3, 4], [5, 6]])
print("rank two ndarray y [[3, 4], [5, 6]]: ")
print(y)
print("---")

# vertical stacking
z = np.vstack((x, y))
print("vertical stacked array: ")
print(z)
print("---")

# horizontal stacking, note that we need to reshape it
w = np.hstack((y, x.reshape(2, 1)))
print("horizontal stacked array: ")
print(w)
