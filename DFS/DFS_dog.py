# def DFS(max_w, num):
#     if num > n:
#         if max_w > c:
#             return
#     else:
#         DFS(max_w+weight[num], num+1)
#         DFS(max_w, num+1)


# if __name__=="__main__":
#     weight = []
#     max_w = 0
#     c, n = map(int, input().split())
#     for i in range(n):
#         weight.append(int(input()))
#     DFS(0, 0)

def DFS(L, sum):
    global result
    if sum > c:
        return
    if L == m:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+ch[L])
        DFS(L+1, sum)

if __name__=="__main__":
    c, m = map(int, input().split())
    ch = [0]*(m+1)
    result = -2147000000
    for i in range(m):
        ch[i] = int(input())
    DFS(0, 0)
    print(result)
