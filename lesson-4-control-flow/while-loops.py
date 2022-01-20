def screen_split(screen_number=80):
    print('-' * screen_number)


print("Factorials with While Loops:")
number = 3
product = 1
current = 1

while current <= number:
    product *= current
    current += 1

print(product)


screen_split()
print("Factorials with For Loops:")
number = 6
product = 1

for i in range(2, number + 1):
    product *= i

print(product)


screen_split()
print("Count By:")

start_num = 12
end_num = 42
count_by = 2
break_num = start_num

while break_num < end_num:
    break_num += count_by

print(break_num)


screen_split()
print("Count By Check")

start_num = 12
end_num = 10
count_by = 2
break_num = start_num
result = 0

if start_num > end_num:
    print("Oops! Looks like your start value is greater than the end value. Please try again.")
else:
    while break_num < end_num:
        break_num += count_by
    result = break_num

print(result)


screen_split()
print("Nearest Square:")

limit = 40
nearest_square = 0
current = 0

while (current + 1) ** 2 < limit:
    current += 1

nearest_square = current ** 2

print(nearest_square)


screen_split()
print("Is odd:")

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87,
            23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_numbers_count = 0
odd_numbers_sum = 0

while (odd_numbers_count < 5) and (i < len(num_list)):
    if num_list[i] % 2 != 0:
        odd_numbers_sum += num_list[i]
        odd_numbers_count += 1
    i += 1

print("Odd numbers count: {}. Odd number sum: {}".format(odd_numbers_count, odd_numbers_sum))
