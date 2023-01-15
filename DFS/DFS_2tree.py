# def DFS(v):
#     if v>7:
#         return
#     else:
#         print(v)
#         DFS(v*2)
#         DFS(v*2+1)


# if __name__=="__main__":
#     DFS(1)

# 전위순회
def DFS(x):
    if x > 7:
        return
    else:
        print(x, end=' ')
        DFS(x*2)
        DFS(x*2+1)

if __name__=="__main__":
    DFS(1)


# 중위순회
def DFS(x):
    if x > 7:
        return
    else:
        DFS(x*2)
        print(x, end=' ')
        DFS(x*2+1)

if __name__=="__main__":
    DFS(1)


# 후위순회
def DFS(x):
    if x > 7:
        return
    else:
        DFS(x*2)
        DFS(x*2+1)
        print(x, end=' ')

if __name__=="__main__":
    DFS(1)