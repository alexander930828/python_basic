# n = int(input())

# for i in range(n):
#     N, s, e, k = map(int, input().split())
#     nums = list(map(int, input().split()))

#     arr=[]

#     for j in range(1, N+1):
#         if s<= j <=e:
#             arr.append(nums[j-1])

#     arr.sort()

#     print(i+1, arr[k-1])


T=int(input())
for i in range(T):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    num=num[s-1:e]
    num.sort()
    print("#%d %d" %(T, num[k-1]))