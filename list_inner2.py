a=[23, 12, 36, 53, 19]

# print(a[:3])
# print(a[1:4])
# print(len(a))

# for i in range(len(a)):
#     print(a[i], end=' ')
# print()

# for x in a:
#     print(x, end=' ')


# for x in enumerate(a):
#     print(x)

# b=(1, 2, 3, 4, 5)
# print(b)

# for index, value in enumerate(a):
#     print(index, value)
# print()

if any(1>x for x in a):
    print("YES")
else:
    print("NO")