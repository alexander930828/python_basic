# n = int(input())
# a = list(map(int, input().split()))

# lt = 0 
# rt = n-1
# last = 0
# res = "" # 문자열
# tmp = [] # 튜플을 담을 공간

# while lt<=rt:
#     if a[lt] > last:
#         tmp.append((a[lt], 'L'))
#     if a[rt] > last:
#         tmp.append((a[rt], 'R'))
#     tmp.sort()
#     if len(tmp) == 0:
#         break
#     else:
#         res = res+tmp[0][1]
#         last = tmp[0][0]
#         if tmp[0][1] == "L":
#             lt += 1
#         else:
#             rt += 1
#     tmp.clear()

# print

# n = int(input())
# a = list(map(int, input().split()))

# last = 0
# res = ""
# tmp = []
# lt = 0 # 양 끝을 비교해야하는 경우에는
# rt = n-1

# while lt<=rt:
#     if a[lt] > last:
#         tmp.append((a[lt], "L"))
#     if a[rt] > last:
#         tmp.append((a[rt], "R"))
#     tmp.sort()
#     if len(tmp) == 0:
#         break
#     else:
#         res = res+tmp[0][1]
#         last = tmp[0][0]
#         if tmp[0][1] == "L":
#             lt += 1
#         else:
#             rt -= 1
#     tmp.clear()

# print(len(res))
# print(res)

n = int(input())
a = list(map(int, input().split()))

last = 0
res = ""
tmp = []

lt = 0
rt = n-1

while lt<=rt:
    if a[lt] > last:
        tmp.append((a[lt], "L"))
    if a[rt] > last:
        tmp.append((a[rt], "R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        last = tmp[0][0]
        res = res+tmp[0][1]
        if tmp[0][1] == "L":
            lt += 1
        else:
            rt -= 1
        tmp.clear()

print(len(res))
print(res)