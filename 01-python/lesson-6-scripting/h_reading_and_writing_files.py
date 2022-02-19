f = open('fruits.txt', 'r')  # r means read only
file_data = f.read()
print(file_data)
f.close()  # close the file and free up any system resources taken up by the file


# we always must close the files, because if we don't, OS can't handle that many resources.
# files = []
# for i in range(10000):
#     try:
#         files.append(open('fruits.txt', 'r'))
#         print(i)
#     except Exception as e:
#         print('Oh, ok, we got into the limit.')
#         print(e)
#         break

# writing:
f = open('brazilian_foods.txt', 'w')  # if this file doesn't exist, python will create it :D
f.write('Brigadeiro, Coxinha, Strogonoff, Acarajé')


# automatically closing the file:

with open('brazilian_foods.txt', 'r') as f:
    file_data = f.read()

print(file_data)
