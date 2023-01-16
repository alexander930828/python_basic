# import sys
# input = sys.stdin.readline

# def DFS(L, time, money):
#     if L == n+1:
#         if sum > res:
#             res = sum
#     else:
#         if L + d[L] <= n+1:
#             DFS(L+d[L], sum+p[L])
#         DFS(L+1, sum)    

# if __name__=="__main__":
#     n = int(input())
#     d = []
#     p = []
#     for i in range(n):
#         day, pay = map(int, input().split())
#         d.append(day)
#         p.append(pay)
#     res = -2147000000
#     d.insert(0, 0)
#     p.insert(0, 0)
#     DFS(1, 0)
#     print(res)

import sys
input = sys.stdin.readline

def DFS(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L + time[L] <= n+1:
            DFS(L+time[L], sum+pay[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n = int(input())
    time = []
    pay = []
    for i in range(n):
        a, b = map(int, input().split())
        time.append(a)
        pay.append(b)
    res = -2147000000
    time.insert(0, 0)
    pay.insert(0, 0)
    DFS(1, 0)
    print(res)