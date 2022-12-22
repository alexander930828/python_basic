n = int(input())
a = list(map(int, input().split()))

num = 0
scr = 0

for i in a:
    if i == 1:
        num +=1
        scr += num
    elif i == 0:
        num = 0

print(scr)


        