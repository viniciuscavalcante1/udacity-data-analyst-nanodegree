def screen_split(screen_number=80):
    print('-' * screen_number)


print("Rewrite this code to be more concise by replacing"
      " the mean function with a lambda expression defined within the call to map().")

# numbers = [
#               [34, 63, 88, 71, 29],
#               [90, 78, 51, 27, 45],
#               [63, 37, 85, 46, 22],
#               [51, 22, 34, 11, 18]
#            ]
#
# def mean(num_list):
#     return sum(num_list) / len(num_list)
#
# averages = list(map(mean, numbers))
# print(averages)

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# def mean(num_list):
#     return sum(num_list) / len(num_list)

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)


screen_split()

print("Rewrite this code to be more concise by replacing the is_short function"
      " with a lambda expression defined within the call to filter().")

# cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
#
# def is_short(name):
#     return len(name) < 10
#
# short_cities = list(filter(is_short, cities))
# print(short_cities)

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)