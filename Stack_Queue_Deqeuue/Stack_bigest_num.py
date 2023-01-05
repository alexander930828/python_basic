# num, m = map(int, input().split())
# num = list(map(int, str(num)))
# print(num)
# stack = []

# for x in num:
#     while stack and m>0 and stack[-1]<x:
#         stack.pop()
#         m -= 1
#     stack.append(x)

# if m != 0:
#     stack = stack[:-m]

# res = ''.join(map(str, stack))

# print(res)


# num, m = map(int, input().split())
# num = list(map(int, str(num)))
# stack = []

# for i in num:
#     while stack and m>0 and stack[-1]<i:
#         stack.pop()
#         m -= 1
#     stack.append(i)

# if m != 0:
#     stack = stack[:-m]

# res = ''.join(map(str, stack))
# print(res)

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for i in num:
    while stack and m>0 and stack[-1]<i: #1번째는 스택이 비어있지 않고 / 2번째는 지울 수 있는 수가 있고, /3번째 스택의 -1이 입력하는 값보다 크면
        stack.pop()
        m -= 1
    stack.append(i)

if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))

print(res)
for i in stack:
    print(i, end='')