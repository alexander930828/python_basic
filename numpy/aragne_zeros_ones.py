import numpy as np

a = np.arange(10)
b = np.zeros((3,2), dtype="int32")
c = np.ones((3,2))
d = a.reshape(-1,2)

print(d)
