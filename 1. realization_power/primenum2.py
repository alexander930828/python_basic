# def reverse(x):
#     res=0
#     while x>0:
#         t = x%10
#         res = res*10 + t
#         x = x // 10
#     return res

# # def isprime(x):
# #     cnt=[0]*214700000
# #     for i in range(2, res+1):
# #         if res % i == 0:
# #             if len(res) == 2:
# #                 print(i)

# def isPrime(x):
#     if x == 1:
#         return False
#     for i in range(2, x//2+1): # 절반까지만 돌아도 된다.
#         if x%i==0:
#             return False
#     else:
#         return True

# n = int(input())
# a = list(map(int, input().split()))

# for x in a:
#     tmp = reverse(x)
#     if isPrime(tmp):
#         print(tmp, end=' ')



def reverse(x):
    res = 0
    while x > 0:
        t = x%10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x): 
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))       

for i in a:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')
    

