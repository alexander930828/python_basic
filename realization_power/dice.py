# def dice(x):
#     for i in range(1, 7):
#         for j in range(1, 7):
#             for k in range(1, 7):
#                 if i == j == k:
#                     return i*1000 + 10000
#                 if i == j != k or i == k != j or i != k == j:
#                     return i*100 + 1000
#                 if i != j != k:
#                     return 

# n = int(input())
# res = 0
# for i in range(n):
#     a, b, c = list(map(int, input().split()))

#     if a==b and b==c:
#         money = 10000+(a*1000) # 제일 확률이 적은 것을 위에다가 걸어야 함
#     elif a==b or a==c:
#         money = 1000+(a*100)
#     elif b==c:
#         money = 1000+(a*100)
#     else:
#         money = c*100
#     if money > res:
#         res = money

# print(res)

n = int(input())
res=0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b ==c:
        money = 10000 + (1000*a)
    elif a == b or a == c:
        money = 1000 + (100*a)
    elif b == c:
        money = 1000 + (100*a)
    else:
        money = c*100
    if money > res: 
        res = money

print(res)


