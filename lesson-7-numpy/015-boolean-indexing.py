import numpy as np

x = np.arange(25).reshape(5, 5)
print(x)

print(x[x > 10])
print(x[x <= 7])
x[(x > 10) & (x < 17)] = -1
print(x)
