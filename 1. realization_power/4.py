# n = int(input())
# a = list(map(int, input().split()))
# avg = (sum(a)/len(a)+0.5)
# min = 10000

# for idx, x in enumerate(a):
#     tmp = abs(avg-x)
#     if tmp < min:
#         min = tmp
#         score = x
#         res = idx + 1
        
#     elif tmp == min:
#         if score < x:
#             scoer = x
#             res = idx + 1
            

# print(score, res)


n = int(input())
a = list(map(int, input().split()))
avg = int(sum(a)/n+0.5)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if  tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(score, res)