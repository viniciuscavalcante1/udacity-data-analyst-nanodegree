def screen_split(screen_number=30):
    print('-' * screen_number)


screen_split()
print('# for iterating over a list:')
sentence = ['I', 'want', 'to', 'eat', 'a', 'burger']

for word in sentence:
    print(word)

screen_split()
print('# for with range')
for number in range(5, 35, 5):
    print(number)


screen_split()
print('# create usernames')
names = ['Vinícius Cavalcante', 'Linda Cavalcante', 'Elvis Cavalcante']
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

screen_split()