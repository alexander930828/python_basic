# s = input()
# stack = []
# cnt = 0

# for i in range(len(s)):
#     if s[i] == '(':
#         stack.append(s[i])
#     else:
#         if s[i-1] == '(':
#             stack.pop()
#             cnt += len(stack)
#         else:
#             stack.pop()
#             cnt += 1

# print(cnt)

# s = input()
# stack = []
# cnt = 0

# for i in range(len(s)):
#     if s[i] == "(":
#         stack.append(s[i])
#     else:
#         if s[i-1] == "(":
#             stack.pop()
#             cnt += len(stack)
#         else:
#             stack.pop()
#             cnt += 1

# print(cnt)

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == "(":
            cnt += len(stack)
        else:
            cnt+=1

print(cnt)