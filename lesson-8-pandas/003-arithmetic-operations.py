import pandas as pd
import numpy as np

fruits = pd.Series([10, 6, 3], ['apples', 'oranges', 'bananas'])
print("Fruits: ")
print(fruits)

print("---")
print("Fruits + 2:")
print(fruits + 2)

print("---")
print("Fruits - 2:")
print(fruits - 2)

print("---")
print("Fruits * 2:")
print(fruits * 2)

print("---")
print("Fruits / 2:")
print(fruits / 2)

#################################
print("------------------")
print("Mathematical functions from numpy:")
print("Square root of fruits: ")
print(np.sqrt(fruits))

print("---")
print("Exponential of each element: ")
print(np.exp(fruits))

print("---")
print("Each element to the power of two:")
print(np.power(fruits, 2))

##############################
print("Specific elements operations:")
print("Bananas plus 2:")
print(fruits['bananas'] + 2)

print("---")
print("Apples minus 2:")
print(fruits.iloc[0] - 2)

print("---")
print("Double oranges and apples: ")
print(fruits[['apples', 'oranges']] * 2)

print("---")
print("Divide apples and oranges with iloc:")
print(fruits.iloc[['apples', 'oranges']] / 2)