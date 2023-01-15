# import sys
# input = sys.stdin.readline

# def DFS(L):
#     global cnt
#     if L == m:
#         for i in range(m):
#             print(res[i], end=' ')
#         print()
#         cnt += 1    
#     else:
#         for i in range(1, n+1):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 res[L] = i
#                 DFS(L+1)
                


# if __name__=="__main__":
#     n, m = map(int, input().split())
#     ch = [0]*(n+1)
#     res = [0]*m
#     cnt = 0 
#     DFS(0)
#     print(cnt)

import sys
sys.stdin.readline

def DFS(L, s):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0, 1)
    print(cnt)