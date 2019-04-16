#Program find the maximum and minimum numbers from a sequence of numbers.


def findNum(data):
   large=data[0]
   small = data[0]
   for num in data:
     if num > large:
        large = num
     elif num < small:
         small = num
   return large, small

print(findNum([0, 10, 15, 40, -5, 42, 17, 28, 75]))


