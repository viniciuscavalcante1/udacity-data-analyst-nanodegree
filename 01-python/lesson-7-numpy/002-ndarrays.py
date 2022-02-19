import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
print(x)
print(type(x))
print(x.dtype)
print(x.shape)
print(x.size)


y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(y)
print(type(y))
print(y.dtype)
print(y.shape)
print(y.size)


z = np.array([1.5, 2.5, 3.5], dtype=np.int32)
print(z)
print(z.dtype)


w = np.array([1, 2, 3, 4, 5])
np.save('my_array', w)

k = np.load('my_array.npy')
print(k)