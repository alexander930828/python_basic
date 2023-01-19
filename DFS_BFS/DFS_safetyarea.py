import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, h):
    ch[x][y] = 1 # 1로 된 부분들은 다녀간 부분이자, 보드가 수위보다 높은 곳
    for i in range(4): # 네 방향을 모두 탐색해버린다 
        xx = x+dx[i] 
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h: #격자판을 벗어나지 않고, 방문하지 않았으며, 보드가 수위보다 높으면 진행
            DFS(xx, yy ,h) #여러번 반복

if __name__=="__main__":
    n = int(input())
    cnt = 0 # 섬의 갯수를 세어주는 변수
    res = 0 # 정답의 체크리스트
    board = [[list(map(int, input().split())) for _ in range(5)]] # 보드는 건들면 안됨
    for h in range(100): #물의 높이를 순회  
        ch = [[0]*n for _ in range(n)] # 다른 물의 높이로 갈때 마다 초기화 해준다.
        cnt = 0 #다른 물의 높이로 갈때마다 섬의 갯수를 초기화 해준다.
        for i in range(n): #여기서 부터 좌표를 통하여 섬을 DFS로 체크해 줄 예정
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h: #만약 체크되어 있지 않고, 보드도 h보다 높다면 
                    cnt+=1 #개수를 하나 추가해주고
                    DFS(i, j, h) #나머지 부분들도 물들여 버리도록 
        res=max(res, cnt) #세어본 갯수랑 비교하여 체크리스트에 저장한다. 
        if cnt==0: #만약 하나도 없다면 브레이크 더 큰 수위는 돌 필요가 없기 때문에 종료해버린다.
            break


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=y<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx, yy, h)



if __name__=="__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    cnt = 0 
    for h in range(100):
        ch = [[0]*5 for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt==0:
            break
    print(res)