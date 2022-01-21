with open('camelot.txt') as song:
    print(song.read(2))  # reads only the first 2 characters
    print(song.read(8))  # reads from 2 to 8 characters
    print(song.read())  # reads the remaining characters that haven't been read yet

camelot_lines = []
with open('camelot.txt') as f:
    for line in f:
        camelot_lines.append(line.strip())  # strip removes the /n

print(camelot_lines)


print("Flying Circus Cast List")


def create_cast_list(filename):
    cast_list = []
    with open(filename) as cast_list_file:
        for actor_line in cast_list_file:
            cast_list.append(actor_line.split(',')[0])

    return cast_list


cast = create_cast_list('flying_circus_cast.txt')
for actor in cast:
    print(actor)


print("Practice Debugging")
# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers
for i in range(10):
    userInput = int(input("Enter any 2-digit number: "))

    # check to see if number is even and if yes, add to list_sum
    # print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))