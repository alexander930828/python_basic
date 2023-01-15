# def DFS(L):
#     if L == m:
#         for j in range(m):
#             print(res[j], end=' ')
#         print()
#         cnt += 1
#     else:
#         for i in range(1, n+1):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 res[L] = i
#                 DFS(L+1)
#                 ch[i] = 0

# if __name__=="__main__":
#     n, m = map(int, input().split())
#     res = [0]*n # 정답 
#     ch = [0]*(n+1) # 중복인지 아닌지 체크하는 것 
#     cnt = 0
#     DFS(0)

import sys
input = sys.stdin.readline

def DFS(L):
    global cnt 
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0: # 조건을 한번 걸어주면 뒤에 함수도 다 적용이 되기 때문에 한번 만 체크할 수 있다. 
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0


if __name__=="__main__":
    n, m = map(int, input().split())
    ch = [0]*(n+1)
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)