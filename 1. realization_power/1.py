n, m = map(int, input().split())

res = []

for i in range(1, n+1):
    if n % i == 0:
        res.append(i)

if len(res) == 0:
    print(-1)

print(res[m-1])