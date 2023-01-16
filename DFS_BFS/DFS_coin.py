# import sys
# input = sys.stdin.readline

# def DFS(L, sum):
#     global res, cnt
#     if sum > t:
#         return
#     if L == len(res):
#         if sum == t:
#             cnt += 1
#     else:
#         DFS(L+1, sum+res[L])
#         DFS(L+1, sum)

# if __name__=="__main__":
#     t = int(input())
#     k = int(input())
#     cnt = 0 
#     res = []
#     for i in range(k):
#         a, b = map(int, input().split())
#         for _ in range(b):
#             res.append(a)
#     DFS(0, 0)
#     print(cnt)

import sys
input = sys.stdin.readline

def DFS(L, sum):
    global cnt
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(num[L]+1):
            DFS(L+1, sum+(coin[L]*i))

if __name__=="__main__":
    t = int(input())
    k = int(input())
    coin = list()
    num = list()
    for i in range(k):
        a, b = map(int, input().split())
        coin.append(a)
        num.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)