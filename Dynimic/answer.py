if __name__=="__main__":
    n, m = map(int, input().split())
    dy = [[5000]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dy[i][i] = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        dy[a][b] = c
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dy[i][j] = min(dy[i][j], dy[i][k]+dy[k][j])
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dy[i][j] == 5000:
                print("M", end=" ")
            else:
                print(dy[i][j], end=" ")
        print()