# if __name__=="__main__":
#     n = int(input) #입력값
#     bricks = []
#     for i in range(n):
#         a, b, c = map(int, input().split()) #벽돌의 대한 정보들을 불러옴
#         bricks.append((a, b, c))
#     bricks.sort(reverse=True) #벽돌이 넓이가 큰 순으로 정렬해 준다
#     dy = [0]*n
#     dy[0] = bricks[0] #벽돌에 대한 다이나믹프로그래밍 
#     res = bricks[0][1] #벽돌의 높이를 측정 
#     for i in range(1, n):
#         max_h: 0
#         for j in range(i-1, -1, -1):
#             if bricks[j][2] > bricks[i][2] and dy[j]>max_h:
#                 max_h = dy[j]
#         dy[i] = max_h + bricks[i][1]
#         res = max(res, dy[i])
#     print(res)

# import sys
# if __name__=="__main__":
#     n = int(input())
#     bricks = []
#     for i in range(n):
#         a, b, c = map(int, input().split())
#         bricks.append((a, b, c))
#     bricks.sort(reverse=True)
#     dy = [0]*n
#     dy[0] = bricks[0][1]
#     res = bricks[0][1]
#     for i in range(1, n):
#         max_h = 0
#         for j in range(i-1, -1, -1):
#             if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
#                 max_h = dy[j]
#         dy[i] = max_h+bricks[i][1]
#         res = max(res, max_h)

#     print(res)

import sys

if __name__=="__main__":
    n = int(input())
    bricks = []
    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True)
    dy = [0]*(n)
    dy[0] = bricks[0][1]
    res = bricks[0][1]
    for i in range(1, n):
        max_h = 0 #탐색하면서 초기화 해준다. 
        for j in range(i-1, -1, -1):
            if bricks[j][2]>bricks[i][2] and dy[j]>max_h:# 가장 높은 높이를 갱신해주는 방법
                max_h = dy[j]
        dy[i] = max_h + bricks[i][1]
        res = max(res, dy[i])
    print(res)