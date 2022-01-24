def screen_split(screen_number=80):
    print('-' * screen_number)


people = ['Vinícius', 'Fernanda', 'Leonardo', 'Carlos', 'Vinícius']

people_counter = {}

for person in people:
    if person not in people_counter:
        people_counter[person] = 1
    else:
        people_counter[person] += 1

print(people_counter)

second_people_counter = {}

for person in people:
    second_people_counter[person] = second_people_counter.get(person, 0) + 1

print(second_people_counter)


screen_split()
professions = {
    "Vinícius": "Data Analyst",
    "Enrico": "Data Engineer",
    "George": "Data Scientist",
    "Lucas": "Analytics Engineer",
    "Monica": "Machine Learning Engineer"
}

for key,value in professions.items():
    print("{}: {}".format(key, value))


screen_split()
fruit_count = 0
not_fruit_count = 0

basket_items = {"apples": 4, "oranges": 19, "kites": 3, "sandwiches": 8, "gnhocchi": 3000}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for key, value in basket_items.items():
    if key in fruits:
        fruit_count += value
    else:
        not_fruit_count += value

print("Fruits: {}, not fruits: {}".format(fruit_count, not_fruit_count))


screen_split()
