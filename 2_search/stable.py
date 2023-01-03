n, m = map(int, input().split())
number = list(map(int, input().split()))

number.sort()

lt = 1
rt = n

while lt<=rt:
    mid = (lt+rt) // 2
    if number[mid] == m:
        print(mid+1)
        break
    elif number[mid] > m:
        rt = mid-1
    else:
        lt = mid+1