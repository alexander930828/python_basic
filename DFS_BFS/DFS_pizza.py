# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def DFS(L, s):
#     global res
#     if L == m: #피자집에서 4개가 선택되면 종료한다.
#         sum = 0 #거리의 합
#         for j in range(len(hs)): #집을 탐색한다
#             x1 = hs[j][0]
#             y1 = hs[j][0]
#             dis = 2147000000 #거리를 최소화 하기 위해서 큰 수를 입력
#             for x in cb: #조합상 선택된 피자집의 좌표를 이용하여
#                 x2 = pz[x][0]
#                 y2 = pz[x][1]
#                 dis = min(dis, abs(x1-x2)+abs(y1-y2)) #거리의 절대 값을 계산해준다
#             sum += dis
#         if sum < res: #마지막으로 계산된거리를 비교하여 최소값을 넣어준다.
#             res = sum
#     else:
#         for i in range(s, len(pz)): #재귀함수를 이용해 피자집에서 4개를 고르는 방법
#             cb[L]=i
#             DFS(L+1, i+1)

# if __name__=="__main__":
#     n, m = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(n)] #입력을 받고
#     hs = []
#     pz = []
#     cb = [0]*m # 조합을 위해서 얼만큼의 변수를 만들지를 설정한다. 
#     res = 2147000000
#     for i in range(n): #여기에서는 보드안에서 집과 피자가게를 분류해준다. 즉, 집과 피자가게의 좌표를 저장해준다.
#         for j in range(n):
#             if board[i][j]==1:
#                 hs.append((i, j))
#             elif board[i][j]==2:
#                 pz.append((i, j))
#     DFS(0, 0)
#     print(sum)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res = sum
    
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0]*m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j]==2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)