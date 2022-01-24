from horizontal_line import horizontal_line


print("Quiz: Compute an Exponent:")

"""It's your turn to import and use the math module.
 Use the math module to calculate e to the power of 3.
  print the answer."""

import math
print(math.exp(3))


horizontal_line()


print("Quiz: Password Generator")

"""Write a function called generate_password that selects three random words
 from the list of words word_list and concatenates them into a single string.
  Your function should not accept any arguments
   and should reference the global variable word_list to build the password."""

import random

word_file = 'words.txt'
word_list = []

with open(word_file) as words:
    for line in words:
        word = line.strip().lower()
        if 3 < len(word) < 8:
            word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words
# concatenated together without spaces


def generate_password(wordlist):
    pass_words = random.choices(wordlist, k=3)
    return pass_words[0] + pass_words[1] + pass_words[2]


print(generate_password(word_list))
