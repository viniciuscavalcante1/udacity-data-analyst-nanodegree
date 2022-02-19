import pandas as pd

# dataframe is a two-dimensional object with labeled rows and columns
# can also hold multiple data types

items = {'Bob': pd.Series([245, 25, 55], index=['bike', 'pants', 'watch']),
         'Alice': pd.Series([40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])}

# row labels of the df are built from the union of the index labels of Series
# column labels of the df are taken from the keys of the dict
shopping_carts = pd.DataFrame(items)
print(shopping_carts)