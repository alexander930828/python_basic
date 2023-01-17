# from collections import deque

# MAX = 10000
# ch = [0]*(MAX+1) # 방문헀는지
# dis = [0]*(MAX+1) # 거리가 몇인지

# n, m = map(int, input().split())
# ch[n] = 1
# dis[n] = 0
# dQ = deque()
# dQ.append(n) # 출발점

# while dQ:
#     now = dQ.popleft() # 5
#     if now==m:
#         break
#     for next in(now-1, now+1, now+5):
#         if 0<next<=MAX:
#             if ch[next]==0:
#                 dQ.append(next)
#                 ch[next] = 1
#                 dis[next] = dis[now]+1

# print(dis[m])

# from collections import deque

# MAX = 10000
# ch = [0]*(MAX+1)
# dis = [0]*(MAX+1)

# n, m = map(int, input().split())
# ch[n] = 1 # 시작점을 방문
# dis[n] = 0
# dQ = deque()
# dQ.append(n)

# while dQ:
#     now = dQ.popleft()
#     if now == m:
#         break
#     for next in(now-1, now+1, now+5):
#         if 0<next<=MAX:
#             if ch[now] == 0:
#                 dQ.append(next)
#                 ch[next] = 1
#                 dis[next] = dis[now] + 1

# from collections import deque

# MAX = 10000
# ch = [0]*(MAX+1)
# dis = [0]*(MAX+1)

# S, E = map(int, input().split())
# dQ = deque()
# dQ.append(S)

# while dQ:
#     now = dQ.popleft()
#     if now == E:
#         print(dis[now])
#         break
#     for next in(now-1, now+1, now+5):
#         if 0<next<=MAX: # -되거나 범위를 넘어가면 안되기 때문에
#             if ch[next] == 0:
#                 ch[next] = 1
#                 dQ.append(next)
#                 dis[next] = dis[now]+1


from collections import deque

MAX = 10000
ch = [0]*(MAX+1)
dis = [0]*(MAX+1)

S, E = map(int, input().split())
ch[S] = 1
dis[S] = 0

dQ = deque()
dQ.append(S)

while dQ:
    now = dQ.popleft()
    if now == E:
        print(dis[now])
        break
    for next in (now-1, now+1, now+5):
        if 0< next<=MAX:
            if ch[next] == 0:
                ch[next] = 1
                dQ.append(next)
                dis[next] = dis[now]+1
 