# N, M = map(int, input().split())
# a = list(map(int, input().split()))
# cnt = 0

# for i in range(N):
#     for j in range(i, N):
#         if a[i:j+1].sum() == M:
#             cnt += 1


N, M = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[lt]
cnt = 0

while True:
    if tot < M:
        if rt<N:
            tot += a[rt]
            rt += 1
        else:
            break

    elif tot == M:
        cnt +=1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)


