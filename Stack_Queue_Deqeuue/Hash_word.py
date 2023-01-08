# n = int(input())

# p = dict()

# for i in range(n):
#     word = input()
#     p[word] = 1
# for i in range(n-1):
#     word = input()
#     p[word] = 0

# for key, value in p.items():
#     if value == 1:
#         print(key)
#         break

# n = int(input())

# p = dict()

# for i in range(n):
#     word = input()
#     p[word] = 1
# for j in range(n-1):
#     word = input()
#     p[word] = 0

# for key, value in p.items():
#     if value == 1:
#         print(key)
#         break

# 각각의 수를 카운트 할때는 딕셔너리를 쓴다.

n = int(input())
p = dict ()

for i in range(n):
    word = input()
    p[word] = 1
for j in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break

