import pandas as pd

groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])

print("Quantity of eggs: ", groceries['eggs'])

print("---")

print("Milk and bread: ")
print(groceries[['milk', 'bread']])

print("---")
print("First element: ", groceries[0])

print("---")
print("Last element: ", groceries[-1])

print("---")
print("First and last element: ", groceries[[0, -1]])

print("---")
# loc is used to explicitly state that we're using a labelled index to search
print("Eggs and apples with loc: ")
print(groceries.loc[['eggs', 'apples']])

print("---")
# attribute iloc stands for integer location and is used to explicitly state that
# we are using a numerical index
print("Indices 2 and 3 with iloc: ")
print(groceries.iloc[[2, 3]])

# pandas series are also mutable like numpy arrays
# which means we can change the elements of a series after it's been created

print("---")
print("Changing the number of eggs")
groceries['eggs'] = 2
print("Eggs: ", groceries['eggs'])

print("---")
print("Dropping apples")
groceries.drop('apples', inplace=True)
print("Updated Series: ")
print(groceries)
