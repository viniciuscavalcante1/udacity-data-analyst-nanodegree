import pandas as pd

items = [{'bikes': 20, 'pants': 30, 'watches': 35}, {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

store_items = pd.DataFrame(items, index=['store 1', 'store 2'])

print("Store_items: ")
print(store_items)

print("---")
print("Bikes: ")
print(store_items[['bikes']])

print("---")
print("Bikes and Pants: ")
print(store_items[['bikes', 'pants']])

print("---------------------")
print("Accessing a row with loc: ")
print(store_items.loc[['store 1']])

print("---")
print(store_items['bikes']['store 2'])