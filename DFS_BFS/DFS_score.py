# import sys
# input = sys.stdin.readline

# def DFS(L, score, time):
#     global res
#     if time > m:
#         return
#     if L==n:
#         if sum > res:
#             res = sum
#     else:
#         DFS(L+1, sum+a[L][0], time+a[L][1])
#         DFS(L+1, sum)



# if __name__=="__main__":
#     a = []
#     res = -2147000000
#     n, m = map(int, input().split())
#     for i in range(n):
#         score, time = map(int, input().split())
#         a.append((score, time))
#     DFS(0, 0, 0)
#     print(res)

import sys
input = sys.stdin.readline

def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+ps[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__=="__main__":
    n, m = map(int, input().split())
    ps = list()
    pt = list()
    for i in range(n):
        score, time = map(int, input().split())
        ps.append(score)
        pt.append(time)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
