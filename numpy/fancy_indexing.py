import numpy as np

array1 = np.array(range(1, 10))

array2 = np.arange(start=1, stop=10)

# print(array1)
# print(type(array1))

array2d = array2.reshape(3,3)
# print(array2d)

# array3 = array1[3:0:-1]
# print(array3)

# array4 = array2d[0:2, 0:2]
array5 = array2d[array2d>5]


print(array1>5)
print(array5)