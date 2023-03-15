# n,k=map(int, input().split())
# num=list(map(int, input().split()))

# num.sort()

# sum=[]

# for i in num:
#     for j in num:
#         if i==j:
#             continue
#         for l in num:
#             if i==l and i==j:
#                 continue
#             sum.append(i+j+l)

# sum = list(set(sum))

# print(sum)

# n, k=map(int, input().split())
# a=list(map(int, input().split()))

# res=set()

# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             res.add(a[i]+a[j]+a[m])

# res=list(res) 
# res.sort(reverse=True)
# print(res[k-1])

n, k= map(int, input().split())
a=list(map(int, input().split()))

res=set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res=list(res)
res.sort(reverse=True)

print(res)
print(res[k-1])