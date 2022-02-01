import time
import numpy as np

x = np.random.random(100000000)

start = time.time()
sum(x) / len(x)
print("Time for calculating the mean without numpy: ", time.time() - start)

start = time.time()
np.mean(x)
print("Time for calculating the mean with numpy: ", time.time() - start)
