# import sys
# input = sys.stdin.readline

# def DFS(L, sum):
#     if L == n:
#         cnt += 1
#     else:

# if __name__=="__main__":
#     n = int(input())
#     a = list(map(int, input().split()))
#     total = sum(a)
#     cnt = 0
#     DFS(0, 0)
#     print(cnt)

import sys
input = sys.stdin.readline

def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        DFS(L+1, sum+g[L])
        DFS(L+1, sum-g[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n = int(input())
    g = list(map(int, input().split()))
    s = sum(g)
    res = set()
    DFS(0, 0)
    print(s - len(res))
    