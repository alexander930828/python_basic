# from collections import deque
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

# ch = [[0]*n for _ in range(n)]
# sum = 0

# mid = n//2

# Q = deque()
# ch[mid][mid] = 1 #처음 방문했던 곳은 무조건 1
# sum += a[mid][mid]

# Q.append((mid, mid))
# L = 0

# while True:
#     if L == mid:
#         break
#     size=len(Q)


from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
mid = n//2

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
res = 0

Q = deque()
Q.append((mid, mid))
ch[mid][mid] = 1
res += a[mid][mid]
L = 0 

while Q:
    size = len(Q)
    if L == mid:
        print(res)
        break
    else:
        for i in range(size):
            tmp = Q.popleft()
            for j in range(4):
                x = (tmp[0]+dx[j])
                y = (tmp[1]+dy[j])
                if ch[x][y] == 0:
                    ch[x][y] = 1
                    res += a[x][y]
                    Q.append((x, y))
    L += 1