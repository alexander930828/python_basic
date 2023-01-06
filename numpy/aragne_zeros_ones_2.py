import numpy as np

# list1 = np.arange(10)

# # print(list1)
# # print(type(list1))

# list2 = np.zeros((3, 2))
# list3 = np.ones((2, 3))

# print(list2)
# print(list3)

# print(list2.reshape(6, 1))

# reshap 를 통해서 차원을 바꿔줄 수 있다.

a = np.arange(10)

array1 = np.array(a)
print(array1.reshape(5, 2).tolist())