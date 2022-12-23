import numpy as np

list = [1, 2, 3]
print(type(list))

array1 = np.array(list)

array2 = np.array([[1, 2, 3],[2, 3, 4]])

print(type(array1))
print(array1.shape)
print(array2.shape)

print(array1.ndim)
print(array2.ndim)