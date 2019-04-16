#Program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

First_ColorList=set(["White", "Black", "Red"])
Second_ColorList =set(["Red", "Green"])

print(First_ColorList.difference(Second_ColorList))

