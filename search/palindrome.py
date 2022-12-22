# n = int(input())

# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(size//2): # 홀수 갯수라 중앙에 있는 것은 비교하지 않아도 된다.
#         if s[j] != s[-1-j]:
#             print("#%d No" %(i+1))
#             break
#     else:
#         print("#%d Yes" %(i+1))


# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s == s[::-1]:
#         print("#%d Yes" %(i+1))
#     else:
#         print("#%d No" %(i+1))

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d No" %(i+1))
            break
    else:
        print("#%d Yes" %(i+1))