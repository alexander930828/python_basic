# import sys
# input = sys.stdin.readline

# def DFS(L, sum):
#     if sum > amt:
#         cnt = 0
#         return
#     if sum == amt:
#         print(cnt)
#     else:
#         for i in range(1, n+1):
            
#             DFS(i, sum+ch[i])
            
#             cnt += 1

# if __name__=="__main__":
#     n = int(input())
#     ch = [0] * n+1
#     for i in range(n):
#         ch[i] = int(input())
#     amt = int(input())
#     res = 214700000
#     DFS(0, 0)
#     print(res)


# def DFS(L, sum):
#     global res
#     if sum > m:
#         return
#     if sum == m:
#         if L < res:
#             res = L
#     else:
#         for i in range(n):
#             DFS(L+1, sum+a[i])
        

# if __name__=="__main__":
#     n = int(input())
#     a = list(map(int, input().split()))
#     m = int(input())
#     res = 2147000000
#     a.sort(reverse=True)
#     DFS(0, 0)
#     print(res)

import sys
input = sys.stdin.readline

def DFS(L, sum):
    global res
    if L > res:
        return # 최소값이 업데이트 되어있는데 그 값보다 더 큰 레벨의 값은 실행할 필요가 없다.
    if sum > m:
        return
    if sum == m:
        if res > L:
            res = L #최소값이 업데이트 되었다.
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    a.sort(reverse=True)
    res = 2147000000
    DFS(0, 0)
    print(res)