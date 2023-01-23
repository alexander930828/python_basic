# def DFS(x, y):
#     if x==0 and y==0:
#         if res < dy[x][y]:
#             res = dy[x][y]
#     else:
#         for i in range(n, -1, -1):
#             for j in range(n, -1, -1):
#                 if 

# if __name__=="__main__":
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     dy = [[0]*n for _ in range(n)]
#     dy[n-1][n-1] = arr[n-1][n-1]
#     for i in range(n, -1, -1):
#         dy[n][i] = dy[n][n+i] + dy[n][i]
#         dy[i][n] = dy[n+i][n] + dy[i][n]
#     res = 2147000000
#     DFS(n-1, n-1)
#     print(res)

def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x==0 and y==0:
        return arr[0][0]
    else:
        if x==0:
            dy[x][y] = DFS(0, y-1) + arr[x][y]
        elif y==0:
            dy[x][y] = DFS(x-1, 0) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
        return dy[x][y]


if __name__=="__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    print(DFS(n-1, n-1))