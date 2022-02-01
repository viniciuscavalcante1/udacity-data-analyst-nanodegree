import numpy as np

x = np.arange(20).reshape(4, 5)
print(x)

z = np.diag(x)
print(z)

w = np.diag(x, k=1)
print(w)

u = np.diag(x, k=-1)
print(u)
