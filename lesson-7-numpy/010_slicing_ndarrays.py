import numpy as np

# 1. ndarray[start:end]  end is always excluded
# 2. ndarray[start:]     start is always included
# 3. ndarray[:end]       end is always excluded

# when slicing, you have to specify a slice for each dimension of the array

print("Slicing a rank two array ")
print("Creating 4x5 array: ")
x = np.arange(1, 21).reshape(4, 5)  # reshape (4 rows, 5 columns)
print(x)

print("---")
print("Slicing and obtaining the last 9 square-shaped values:")
z = x[1:4, 2:5]  # 4 and 5 because the end is exclusive, always remember
print(z)

# another way:
z = x[1:, 2:]

print("---")
print("Slicing and obtaining the first 9 square-shpaed values:")
z = x[:3, :3]
print(z)

print("---")
print("Slicing and obtaining all the values from the last row:")
z = x[:, 3:4]
print(z)

# slicing only creates a view of the original array
# this means that if you make any changes in z, it will also change x

print("---")
print("Proving that slicing only creates a view of the original array and changes "
      "affects both arrays: ")

print("x: ")
print(x)

z = x[1:, 2:]
print("z: ")
print(z)

print("Changing the last element in z to 555: ")
z[2, 2] = 555
print("z: ")
print(z)

print("x: ")
print(x)

# if we want to create a new numpy array that contains a copy of the values in the slice
# we have to use the copy function
