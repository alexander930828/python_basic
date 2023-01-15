# import sys
# sys.stdin.readline

# def DFS(L, s, sum):
#     global cnt
#     if L == n:
#         if sum%m == 0:
#             cnt += 1
#     else:
#         for i in range(s, n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     DFS(L, s+1, sum+a[i]+a[j]+a[k])

# if __name__=="__main__":
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     m = int(input())
#     cnt = 0 
#     DFS(0, 0, 0)
#     print(cnt)

import sys
input = sys.stdin.readline

def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum%m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])

if __name__=="__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)