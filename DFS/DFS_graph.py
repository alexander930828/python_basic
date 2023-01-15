# n, m = map(int, input().split())

# a =[[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     node1, node2, score = map(int, input().split())
#     a[node1][node2] = score

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(a[i][j], end=' ')
#     print()

n, m = map(int, input().split())

g = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()
