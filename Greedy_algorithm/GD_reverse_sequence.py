# n = int(input())
# a = list(map(int, input().split()))

# a.sort()
# seq = [0]*n

# for i in range(n):
#     for j in range(n):
#         if a[i]==0 and seq[j]==0:
#             seq[j] = i+1

n = int(input())
a = list(map(int, input().split()))

seq = [0]*n

for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j] = i+1
            break
        else: 
            a[i] -= 1

for i in seq:
    print(i, end=" ")

