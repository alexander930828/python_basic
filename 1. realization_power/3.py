n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

res = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            res.append(a[i]+a[j]+a[k])

print(res[m-1])
