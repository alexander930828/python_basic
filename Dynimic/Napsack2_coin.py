if __name__=="__main__":
    n = int(input())
    coin = [list(map(int, input().split()))]
    m = int(input())
    dy = [1000]*(m+1)
    for i in range(1, m+1):
        for j in range(n):
            dy[i] = min(dy[i], dy[i-coin[j]]+1)
    print(dy[m])