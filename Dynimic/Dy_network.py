n = int(input())

dm = [0]*(n+1)
dm[1] = 1
dm[2] = 2

for i in range(3, n+1):
    dm[i] = dm[i-1] + dm[i-2]

print(dm[n])