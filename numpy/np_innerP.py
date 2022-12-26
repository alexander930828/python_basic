import numpy as np 

array1 = np.arange(start=1, stop=7)
array2 = np.arange(start=7, stop=13)

array1 = array1.reshape(2, 3)
array2 = array2.reshape(3, 2)

print(array1)
print(array2)

array1 = np.transpose(array1)
array2 = np.transpose(array2)

print(array1)
print(array2)



npdot = np.dot(array1, array2)

print(npdot)