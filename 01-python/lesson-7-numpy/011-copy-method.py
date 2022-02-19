import numpy as np

print("x: ")
x = np.arange(20).reshape(4, 5)
print(x)

print("z (copy of x, sliced): ")
z = np.copy(x[1:, 2:])
print(z)

# alternative using copy as a method:
z = x[1:, 2:].copy()

print("---")
print("Changing the last element of z to 555: ")

z[2, 2] = 555
print("z: ")
print(z)

print("x: ")
print(x)
