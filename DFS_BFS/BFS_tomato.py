from collections import deque

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque() # BFS로 풀이할 때에는 항상 deque를 활용
dis=[[0]*n for _ in range(m)] # 레벨별로 저장을 할꺼기 때문에

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j)) # 보드에서 익은토마토 1인 지점을 탐색해서 Q에 넣어주는 행위

while Q:
    tmp=Q.popleft() # 보드에서 익은토마토가 있는 지점을 꺼내서 탐색을 시작한다
    for i in range(4): # 네 방향을 모두 검사하는데
        xx = tmp[0]+dx[i]
        yy = tmp[1]+dy[i]
        if 0<=xx<m and 0<=yy<n and board[xx][yy]==0: # 범위를 넘어서는지, 또는 안 익은토마토(0)가 있는지 주변에 없으면 스탑.
            board[xx][yy] = 1 # 만약 안익은토마토라면 익은토마토(1)로 변경시켜주고
            dis[xx][yy]=dis[tmp[0]][tmp[1]]+1 #그 탐색한 경우에는 레벨을 + 1 하는데 그 좌표에다가 표시
            Q.append((xx, yy)) # 다음 부분을 탐색 Q에 추가

flag=1 # 플래그를 표시 해놓고 다 익었는지 확인!
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flat=0 #다 익었다면 flag를 0으로

result=0 #익은지 몇일 걸리는지
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result=dis[i][j]
    print(result) #0일만에 다익게 된다면 0으로 출력하기때문에 상관 x
else: # 다 익을 수 없다면 -1
    print(-1)

# from collections import deque

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# col, row = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(row)]
# dis = [[0]*col for _ in range(row)]
# Q = deque()

# for i in range(row):
#     for j in range(col):
#         if board[i][j] == 1:
#             Q.append((i, j))

# while Q:
#     tmp = Q.popleft()
#     for i in range(4):
#         xx = tmp[0]+dx[i]
#         yy = tmp[1]+dy[i]
#         if 0<=xx<row and 0<=yy<col and board[xx][yy]==0:
#             board[xx][yy] = 1
#             dis[xx][yy] = dis[tmp[0]][tmp[1]]+1
#             Q.append((xx, yy))

# # flag = 1
# # for i in range(row):
# #     for j in range(col):
# #         if dis[i][j] != 0:
# #             flag = 0

# # result = 0

# # if flag==1:
# #     for i in range(row):
# #         for j in range(col):
# #             if dis[i][j] > result:
# #                 result = dis[i][j]
# #     print(result)
# # else:
# #     print(-1)

# for i in range(row):
#     for j in range(col):
#         print(dis[i][j], end=' ')
#     print()