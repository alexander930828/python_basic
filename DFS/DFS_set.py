# def DFS(v):
#     if v == n+1:

#     else:
#         ch[v] = 1
#         DFS(v+1)
#         ch[v] = 0
#         DFS(v+1)

# if __name__=="__main__":
#     n = int(input())
#     ch = [0]*(n+1)
#     DFS(1)


def DFS(x):
    if x == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()

    else:
        
        DFS(x+1)
        ch[x] = 1
        DFS(x+1)
        ch[x] = 0

if __name__=="__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)