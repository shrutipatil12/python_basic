#Program to get execution time for a Python method.

import time

Str=["shruti", "Patil"]
list=[2, 3, 4, 5]
start_time = time.time()
result=(Str+list)
print("Concatenated String is =" ,result)
end_time = time.time()
res=end_time - start_time
print(res)
print("\nResult of concatenation is ", result)
print("and required time to calculate is :", res)


