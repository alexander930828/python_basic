# a=[0]*10 # 10개의 0리스트가 생김

a=[[0]*3 for _ in range(3)]

a[0][1]=1
a[1][1]=2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()