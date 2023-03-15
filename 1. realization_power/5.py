# n, m = map(int, input().split())
# num = [0]*(m+n+3)
# maxnum = 0

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         num[i+j] += 1

# for i in range(n+m+3):
#     if num[i] > maxnum:
#         maxnum = num[i]

# for i in range(n+m+3):
#     if num[i] == maxnum:
#         print(i, end=" ")


n, m  = map(int, input().split())
cnt = [0]*(n+m+1)
maxnum = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(1, n+m+1):
    if cnt[i] > maxnum:
        maxnum = cnt[i]

for i in range(1, n+m+1):
    if cnt[i] == maxnum:
        print(i, end=" ")