import pandas as pd

# pandas series is a one-dimensional array-like object that can hold
# many data types (numpy can only hold one data type) and you can
# assign an index label to each element in the pandas series

groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print("Pandas series of groceries:")
print(groceries)

print("---")

print("Shape: ", groceries.shape)  # sizes of each dimension of the data

print("---")

print("Number of dimensions: ", groceries.ndim)

print("---")

print("Total number of values in the array: ", groceries.size)

print("---")

print("Indexes: ", groceries.index)

print("---")

print("Data/values: ", groceries.values)

print("---")

print("Checking if an index exists (banana):")
print('banana' in groceries)

print("---")

print("Checking if an index exists (bread):")
print('bread' in groceries)