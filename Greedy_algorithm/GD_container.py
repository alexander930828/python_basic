l = int(input())
box = list(map(int, input().split()))
move = int(input())
cnt = 0

while cnt < move:
    box.sort()
    box[0] += 1
    box[-1] -= 1
    cnt += 1

ans = max(box) - min(box)

print(ans)