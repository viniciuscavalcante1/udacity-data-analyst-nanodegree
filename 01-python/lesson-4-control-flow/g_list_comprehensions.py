def screen_split(screen_number=80):
    print('-' * screen_number)


print("Without list comprehension:")

cities = ['são paulo', 'rio de janeiro', 'indaiatuba', 'campinas']

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)


screen_split()
print("With List Comprehensions:")
capitalized_cities = [city.title() for city in cities]

print(capitalized_cities)


screen_split()
print("Without list comprehensions:")
squares = []
for x in range(9):
    squares.append(x**2)
print(squares)


screen_split()
print("With list comprehensions:")
squares_list_comprehensions = [x**2 for x in range(9)]
print(squares_list_comprehensions)


screen_split()
print("List comprehensions with conditionals:")
squares_list_comp_with_conditions = [x**2 for x in range(9) if x % 2 == 0]
print(squares_list_comp_with_conditions)


screen_split()
print("List comprehensions with conditionals if and else")
squares_if_else = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares_if_else)
