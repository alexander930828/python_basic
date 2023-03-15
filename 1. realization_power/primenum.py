# n = int(input())
# num = [0]*(n+1) # 하나더 추가해줘야 원하고자하는 수까지 만든다.
# cnt = 0

# for i in range(2, n+1):
#     if num[i]==0:
#         cnt+=1
#         for j in range(i, n+1):
#             if j%i==0:
#                 num[j]=1

# print(cnt)

n = int(input())
num = [0]*(n+1) # 하나더 추가해줘야 원하고자하는 수까지 만든다.
cnt = 0

for i in range(2, n+1):
    if num[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            num[j]=1

print(cnt)