#Program to sort three integers.

First_num=int(input("Enter first number to sort"))
Second_num=int(input("Enter second number to sort"))
Third_num=int(input("Enter third number to sort"))

num1 = min(First_num, Second_num, Third_num)
num3 = max(First_num, Second_num, Third_num)
num4=num1+num3
num2 = (First_num + Second_num + Third_num) -num4
print("Sorted list ", num1, num2, num3)
