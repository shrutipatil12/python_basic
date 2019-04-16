#Program to get numbers divisible by fifteen from a list using an anonymous function.


number= [40, 75, 60, 33, 10, 110]

result =tuple(filter(lambda divide: (divide % 15 == 0), number))
print("Numbers divisible by 15 are=  ",result)