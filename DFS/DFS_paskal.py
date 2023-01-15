import sys
input = sys.stdin.readline

def DFS(L, sum):
    if L == n and sum == f:
        for j in p:
            print(j, end=' ')
        sys.exit(0)
    else:
        for k in range(1, n+1):
            if ch[k] == 0:
                ch[k] = 1
                p[L] = k
                DFS(L+1, sum+(p[L]*b[L]))
                ch[k] = 0

if __name__=="__main__":
    n, f = map(int, input().split())
    ch = [0]*(n+1)
    p = [0]*n
    b = [1]*n
    for i in range(1, n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)    