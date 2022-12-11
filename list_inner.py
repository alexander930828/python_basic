import random as r

# a=[1, 2, 3, 4 ,5]
# #print(a)

# b=list(range(1, 11))
# #print(b)

# c=a+b
# #print(c)

# print(a)
# a.append(6)
# print(a)

# a.insert(3, 7)
# print(a)
# a.pop()
# a.pop(3)
# print(a)

# a.remove(4)
# print(a)

# print(a.index(5))

a=list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))

r.shuffle(a)
print(a)
a.sort()
a.sort(reverse=True)
print(a)

a.clear()
print(a)