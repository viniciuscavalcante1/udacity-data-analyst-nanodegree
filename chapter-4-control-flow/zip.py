def screen_split(screen_number=80):
    print('-' * screen_number)


print("Zipping two lists:")
items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']

weights = [15, 34, 42, 120, 5]

print(list(zip(items, weights)))

for cargo in zip(items, weights):
    print(cargo[0], cargo[1])


screen_split()
print("Unzipping a list:")

manifest = [('bananas', 15), ('mattresses', 34), ('dog kennels', 42), ('machine', 120), ('cheeses', 5)]

items, weights = zip(*manifest)

print(items)
print(weights)