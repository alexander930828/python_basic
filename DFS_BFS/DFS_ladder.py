def DFS(x, y):
    ch[x][y] = 1 #지나간 자리는 1로 체크
    if x==0: #만약 x가 0이라면 y출력 행에 다 도달했다면 종료되면서 원하는 값을 출력하게 된다. 
        print(y)
    else: # 범위를 중요하게 생각하는데 
        if y-1>0 and board[x][y-1]==1 and ch[x][y-1]==0: #왼쪽으로 가는 경우 
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0: #오른쪽으로 가는 경우
            DFS(x, y+1)
        else: # 왼쪽 오른쪽 모두 못갈때 
            DFS(x-1, y)



if __name__=="__main__":
    board = [list(map(int, input().split())) for _ in range(10)] #보드 입력을 해준다
    ch = [[0]*10 for _ in range(10)] #지나간 자리는 체크를 해주기 위해서 만든다
    for y in range(10): #시작점으로 부터 체크를 하기위해서 
        if board[9][y] == 2: #만약 마지막열에 있는2가 이 지점이라면 여기서 부터 탐색 시작
            DFS(9, y) #행이 0으로 갈때까지 탐색

# def DFS(x, y):
#     ch[x][y] = 1
#     if x == 0:
#         print(y)
#     else:
#         if y-1>0 and ch[x][y-1]==0 and board[x][y-1]==1:
#             DFS(x, y-1)
#         elif y+1<10 and ch[x][y+1]==0 and board[x][y+1]==1:
#             DFS(x, y+1)
#         else:
#             DFS(x-1, y)

# if __name__=="__main__":
#     board = [list(map(int, input().split())) for _ in range(10)]
#     ch = [[0]*10 for _ in range(10)]
#     for y in range(10):
#         if board[9][y] == 2:
#             DFS(9, y)