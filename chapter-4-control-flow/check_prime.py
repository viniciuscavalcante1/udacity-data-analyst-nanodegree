check_prime = [26, 39, 51, 53, 57, 79, 85]

for number in check_prime:
    for num in range(2, number):
        if number % num == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(
                number, num, number
            ))
            break
        if num == number - 1:
            print("{} IS a prime number".format(number))
