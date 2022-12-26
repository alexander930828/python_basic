import numpy as np

array1 = np.arange(start=1, stop=10)
array2d = array1.reshape(3,3)

# print(array1)
# print(array2d)

array3 = np.sort(array2d, axis=1)

# print(array3)

org_array = np.array([3, 1, 9, 5])

snp = np.argsort(org_array)[::-1]

print(snp)