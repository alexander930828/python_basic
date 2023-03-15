n = int(input())
for i in range(2):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = arr[s-1: e]
    res.sort()
    print("#%d %d" %(i+1, res[k-1]))
    