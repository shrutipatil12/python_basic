#Program to determine if variable is defined or not.

try:
    number= 12
except NameError:
    print("Variable is not defined.")
else:
    print("Variable is defined.")

try:
    size
except NameError:
    print("Variable is not defined.")
else:
    print("Variable is defined.")
