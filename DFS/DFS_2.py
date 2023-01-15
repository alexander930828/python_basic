# def DFS(x):
#     if x==0:
#         return
#     else:
#         DFS(x//2)
#         print(x%2, end='')


# if __name__=="__main__":
#     n = input()
#     DFS(n)


def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='') # 이진수는 나머지를 기록해주는 것  



if __name__=="__main__":
    n = input()
    DFS(n)