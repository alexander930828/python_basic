# import sys
# input = sys.stdin.readline

# def DFS(L, plus):
#     global tmp
#     if L == n:
#         if tmp < min_n:
#             tmp = max(res) - min(res)
#             res.clear()
#     else:
#         for i in range(3):
#             money[i]+=coin[L]
#             DFS(L+1)
#             money[i]-=coin[L]

# if __name__=="__main__":
#     n = int(input())
#     coin = []
#     for _ in range(n):
#         coin.append(int(input()))
#     money=[0]*3
#     min_n = 2147000000
#     DFS(0)
#     print(tmp)

import sys 
input = sys.stdin.readline


def DFS(L):
    global res
    if L == n:
        tmp = set()
        for i in money:
            tmp.add(i)
        if len(tmp) == 3:
            cha = max(money) - min(money)
            if cha < res:
                res = cha
    
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]


if __name__=="__main__":
    n = int(input())
    coin = []
    money = [0]*3
    for i in range(n):
        coin.append(int(input()))
    res = 2147000000
    DFS(0)
    print(res)