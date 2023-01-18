# from collections import deque

# maze = [list(map(int, input().split())) for _ in range(7)]
# ch = [[0]*7 for _ in range(7)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# dq = deque()
# ch[0][0] = 1
# maze[0][0] = 1
# dq.append((1, 1))

# cnt = 0
# res = 214700000

# while dq:
#     for j in dq:
#         tmp = dq.popleft()
#         for i in range(4):
#             x = tmp[0]+dx[i]
#             y = tmp[1]+dy[i]
#             if ch[x][y] == (6, 6):
#                 break
#             elif ch[x][y] == 0:
#                 ch[x][y] = 1
#                 dq.append((x, y))
#                 cnt += 1



from collections import deque

board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]

dq = deque()
board[0][0] = 1
dq.append((1,1))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while dq:
    tmp = dq.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]]+1
            dq.append((x, y))
if dis[6][6] == 0:
    print(-1)

