# Program to accept numbers and generate List and Tuple from those numbers.


size = input("Enter the numbers: ")
list = size.split(",")
tuple = tuple(list,)

print('List : ',list)
print('Tuple : ',tuple)