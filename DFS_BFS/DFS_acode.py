import sys
input = sys.stdin.readline


def DFS(L, P):
    if L == n:
        cnt += 1
        for j in range(P):
            print(res[j], end=' ')
        print()

    else:
        for i in range(1, 27):
            if code[L]==i:
                res[P]==i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
                res[P] == i
                DFS(L+2, P+1) 
                

if __name__=="__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0]*(n+3)
    cnt = 0
    DFS(0, 0)