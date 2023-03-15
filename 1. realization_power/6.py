# def digit_sum(x):
#     sum_n = 0
#     while x>0:
#         sum_n += (x % 10)
#         x = x//10
#     return sum_n

# if __name__=="__main__":
#     n = int(input())
#     num = list(map(int, input().split()))
#     max_n = -2147000000
#     for i in num:
#         tmp = digit_sum(i)
#         if tmp > max_n:
#             max_n = tmp
#             ans = i
#     print(ans)


def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum

if __name__=="__main__":
    n = int(input())
    num = list(map(int, input().split()))
    max_n = -2147000000
    for i in range(n):
        tmp = digit_sum(num[i])
        if tmp > max_n:
            max_n = tmp
            res = num[i]
    print(res)
            
