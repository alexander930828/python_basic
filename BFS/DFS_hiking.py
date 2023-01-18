# import sys 
# input = sys.stdin.readline

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def DFS(x, y):
#     global cnt
#     if x==4 and y==4:
#         cnt += 1
#     else:
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0<=xx<=4 and 0<=yy<=4 and ch[xx][yy]==0:
#                 if road[x][y] < road[xx][yy]:
#                     ch[xx][yy] = 1
#                     DFS(x+1, y+1)
#                     ch[xx][yy] = 0

# if __name__=="__main__":
#     n = int(input())
#     road = [list(map(int, input().split())) for _ in range(5)]
# #     ch = [[0]*n for _ in range(n)]
# #     ch[0][0] = 1
# #     cnt = 0
# #     DFS(0, 0)
# #     print(cnt)

# import sys
# input = sys.stdin.readline

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def DFS(x, y):
#     global cnt
#     if x==ex and y==ey:
#         cnt+1
#     else:
#         for k in range(4):
#             xx = x+dx[k]
#             yy = y+dy[k]
#             if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
#                 ch[xx][yy] = 1
#                 DFS(xx, yy)
#                 ch[xx][yy] = 0


# if __name__=="__main__":
#     n = int(input())
#     board = [[0]*n for _ in range(n)]
#     ch = [[0]*n for _ in range(n)]
#     max = -2147000000
#     min = 2147000000
#     for i in range(n):
#         tmp = list(map(int, input().split()))
#         for j in range(n):
#             if tmp[j] < min:
#                 min = tmp[j]
#                 sx = i
#                 sy = j
#             if tmp[j] > max:
#                 max = tmp[j]
#                 ex = i
#                 ey = j
#             board[i][j] = tmp[j]
#     ch[sx][sy] = 1
#     cnt = 0
#     DFS(sx, sy)
#     print(cnt)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


if __name__=="__main__":
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]
    ch[sx][sy] == 1
    DFS(0, 0)
    print(cnt)