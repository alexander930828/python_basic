# n, m = map(int, input().split())
# body = list(map(int, input().split()))

# body.sort()
# amt = 0
# cnt = 1

# for i in body:
#     if amt == 0:
#         cnt += 1
#     elif amt < m:
#         amt = amt + i
#     else:
#         cnt += 1
#         amt = 0

# print(cnt)

# n, limit = map(int, input().split())
# p = list(map(int, input().split()))
# p.sort()

# cnt = 0

# while p: #p가 비어있으면 멈추게 됨
#     if len(p) == 1:
#         cnt += 1 
#         break
#     if p[0] + p[-1] > limit:
#         p.pop()
#         cnt += 1
#     else:
#         p.pop(0)
#         p.pop()
#         cnt += 1

# print(cnt)

n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
cnt = 0 

while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.pop()
        p.pop(0)
        cnt += 1

print(cnt)