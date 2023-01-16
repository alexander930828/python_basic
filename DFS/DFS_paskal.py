# import sys
# input = sys.stdin.readline

# def DFS(L, sum):
#     if L == n and sum == f:
#         for j in p:
#             print(j, end=' ')
#         sys.exit(0)
#     else:
#         for k in range(1, n+1):
#             if ch[k] == 0:
#                 ch[k] = 1
#                 p[L] = k
#                 DFS(L+1, sum+(p[L]*b[L]))
#                 ch[k] = 0

# if __name__=="__main__":
#     n, f = map(int, input().split())
#     ch = [0]*(n+1)
#     p = [0]*n
#     b = [1]*n
#     for i in range(1, n):
#         b[i] = b[i-1]*(n-i)//i
#     DFS(0, 0)

import sys
input = sys.stdin.readline

def DFS(L, sum):
    if L == n and sum == f:
        for i in p:
            print(i, end= ' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i # L이 2일 때는, 
                DFS(L+1, sum+(p[i]*b[i]))
                ch[i] = 0

if __name__=="__main__":
    n, f = map(int, input().split())
    ch = [0]*(n+1)
    p = [0]*n # 내가 입력 할 수 
    b = [0]*n # 파스칼의 삼각형 가중치 수열
    for i in range(1, n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)