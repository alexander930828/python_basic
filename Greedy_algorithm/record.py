# def Count(capacity):
#     cnt = 1
#     Sum = 0
#     for x in Music:
#         if Sum+x > capacity:
#             cnt += 1
#             Sum = x
#         else:
#             Sum += x
#     return cnt


# n, m = map(int, input().split())
# Music = list(map(int, input().split()))

# lt = 1
# rt = sum(a)
# res = 0 

# while lt<=rt:
#     mid = (lt+rt)//2
#     if Count(mid) <= m:
#         res = mid
#         rt = mid-1
#     else:
#         lt = mid+1

# print(res)

def Count(capacity):
    cnt = 1
    Sum = 0
    for x in Music:
        if Sum + x > capacity:
            cnt += 1
            Sum = x
        else:
            Sum += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))

lt = 1
rt = sum(Music)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1

print(res)