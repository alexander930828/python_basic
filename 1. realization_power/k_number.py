# n,k= map(int, input().split())

# cnt=0

# for i in range(1, k+1):
#     if n%i==0:
#         cnt+=1
#     if cnt==k:
#         print(i)
#         break
# else:
#     print(-1)

n,k=map(int, input().split())

cnt=0

for i in range(1, n+1):
    if n%i==0:
        cnt+=1 # 약수가 있을 때만 올라가니 즉. 카운트 된 수가 약수의 인덱스가 되어버린다. 
    if cnt==k:
        print(i)
        break
else:
    print(-1)