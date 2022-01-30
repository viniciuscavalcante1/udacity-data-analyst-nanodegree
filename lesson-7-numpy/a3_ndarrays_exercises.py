print("Quiz: ABC's")

"""Create a numpy array of strings containing letters 'a' through 'j' (inclusive)
 of the alphabet. Then, use numpy array attributes to print
  the following information about this array:

dtype of array
shape of array
size of array
"""

import numpy as np
letter_array = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k'])
print("Letter Array: ", letter_array)

print("Array dtype: ", letter_array.dtype)

print("Array shape: ", letter_array.shape)

print("Array size: ", letter_array.size)