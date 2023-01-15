# import sys
# input = sys.stdin.readline

# def DFS(v):
#     if v==n:
#         cnt+=1
#     else:
#         for i in range(1, n+1):
#             if g[v][i] == 1 and ch[i] == 0:
#                 ch[i] = 1
#                 DFS(i)
#                 ch[i] = 0

# if __name__=="__main__":
#     n, m = map(int, input().split())
#     g = [[0]*(n+1) for _ in range(n+1)]
#     ch = [0]*(n+1)
#     for _ in range(m):
#         a, b = map(int, input().split())
#         g[a][b] = 1
#     cnt = 0
#     ch[1] = 1
#     DFS(1)

# import sys
# input = sys.stdin.readline

# def DFS(v):
#     global cnt
#     if v == n:
#         cnt += 1
#         for x in path:
#             print(x, end=' ')
#         print()    
#     else:
#         for i in range(1, n+1):
#             if g[v][i] == 1 and ch[i] == 0: # 길이 있는 곳과 여기에서 방문하지 않은 곳을 탐색 
#                 ch[i] = 1
#                 path.append(i)
#                 DFS(i)
#                 path.pop()
#                 ch[i] = 0


# if __name__=="__main__":
#     n, m = map(int, input().split())
#     g = [[0]*(n+1) for _ in range(n+1)]
#     ch = [0]*(n+1)
#     for _ in range(m):
#         a, b = map(int, input().split())
#         g[a][b] = 1
#     cnt = 0
#     path = []
#     path.append(1)
#     ch[1] = 1
#     DFS(1)
#     print(cnt)

import sys
input = sys.stdin.readline

def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        for i in path:
            print(i, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i] = 0
                path.pop()


if __name__=="__main__":
    n, m = map(int, input().split())
    g = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    ch = [0]*(n+1)
    ch[1] = 1
    path = []
    path.append(1)
    DFS(1)
    print(cnt)