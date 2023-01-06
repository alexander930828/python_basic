# from collections import deque

# need = input()
# n = int(input())
# for i in range(n):
#     plan = input()
#     dq = deque(need)
#     for x in plan: # dq안에 없는 것은 다 걸러짐
#         if x in dq:
#             print(dq)
#             if x != dq.popleft():
                
#                 print("#%d No" %(i+1))
#                 break
#     else:
#         if len(dq) == 0:
#             print("#%d YES" %(i+1))
#         else:
#             print("#%d No" %(i+1))

from collections import deque

need = input()
dq = deque(need)
n = int(input())
for i in range(n):
    study = input()
    for x in study:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))