# def Count(len):
#     cnt = 0
#     for x in line:
#         cnt += (x//len)
#     return cnt

# k, n = map(int, input().split())
# line = [] 
# res = 0
# largest = 0

# for i in range(k):
#     tmp = int(input())
#     line.append(tmp)
#     largest = max(largest, tmp)

# lt = 1
# rt = largest

# while lt<=rt:
#     mid = (lt+rt)//2
# #     if Count(mid) >= n:
# #         res = mid
# #         lt = mid+1
# #     else:
# #         rt = mid-1

# # print(res)

# # def Count(len):
# #     cnt = 0
# #     for x in a:
# #         cnt += (x//len)
# #     return a

# # k, n = map(int, input().split())
# # a = []
# # largest = 0 
# # res = 0

# # for i in range(k):
# #     tmp = int(input())
# #     a.append(tmp)
# #     largest = max(largest, tmp)

# # lt = 0
# # rt = largest

# # while lt <= rt:
# #     mid = (lt+rt)//2
# #     if Count(mid) >= n:
# #         res = mid
# #         lt += mid+1
# #     else:
# #         rt = mid-1

# def Count(len):
#     cnt = 0 
#     for x in line:
#         cnt += (x//len)
#     return cnt    

# k, n = map(int, input().split())
# line = []
# res = 0
# largest = 0

# for i in range(k):
#     tmp = int(input())
#     line.append(tmp)
#     largest = max(largest, tmp)

# lt = 1
# rt = largest

# while lt <= rt:
#     mid = (lt+rt)//2
#     if Count(mid) >= n:
#         res = mid
#         lt = mid+1
#     else:
#         rt = mid-1

# print(res)

def Count(Len):
    cnt = 0
    for x in line:
        cnt += (x//Len)
    return cnt 
    
k, n = map(int, input().split())
line = []
largest = 0
res = 0 

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)     