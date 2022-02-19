def screen_split(screen_number=80):
    print('-' * screen_number)


print("1 - Population Density Function")
# Write a function named population_density that takes two arguments,
# population and land_area, and returns a population density calculated from those values.
# I've included two test cases that you can use to verify that your function works correctly.
# Once you've written your function, use the Test Run button to test your code.


def population_density(population, land_area):
    return population / land_area


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


screen_split()
print("2 - readable_timedelta")
# Write a function named readable_timedelta.
# The function should take one argument, an integer days, and return a string that says how many weeks
# and days that is. For example, calling the function and printing the result like this:


def readable_timedelta(days):
    return "{} week(s) and {} day(s).".format(int(days / 7), days % 7)


print(readable_timedelta(507))