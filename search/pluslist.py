# n = int(input())

# word = []

# for i in range(n):
#     s = input().split()
#     for j in s:
#         word.append(j)

# word = list(map(int, word))
# word.sort()

# for k in word:
#     print(k, end=' ')


# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# p1=p2=0
# c=[]

# while p1<n and p2<m:
#     if a[p1] <= b[p2]:
#         c.append(a[p1])
#         p1+=1
#     else:
#         c.append(b[p2])
#         p2+=1
# if p1<n:
#     c=c+a[p1:]
# if p2<m:
#     c=c+b[p2:]

# for x in c:
#     print(x, end=' ')


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c = []
p1 = p2 = 0

while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1<n:
    c = c+a[p1:]
if p2<m:
    c = c+b[p2:]

for j in c:
    print(j, end=' ')