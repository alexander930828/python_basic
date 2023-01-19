dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx, yy)
    

if __name__=="__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt=0
                DFS(i, j)
    print(cnt)