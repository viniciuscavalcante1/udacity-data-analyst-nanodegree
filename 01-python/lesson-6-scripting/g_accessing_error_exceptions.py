try:
    print(30/0)
except ZeroDivisionError as e:
    print("ZeroDivisionError ocurred: {}".format(e))


try:
    print(name)
except Exception as e:
    print("Exception occurred: {}".format(e))