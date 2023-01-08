# word1 = input()
# word2 = input()

# list = dict()

# for i in word1:
#     list[i] += 1

# print(list)

# a = input()
# b = input()

# str1 = dict()
# str2 = dict()

# for x in a:
#     str1[x] = str1.get(x, 0)+1
# for x in b:
#     str1[x] = str1.get(x, 0)+1
    
# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break

# else:
#     print("YES")


# a = input()
# b = input()

# str1 = dict()
# str2 = dict()

# for i in a:
#     str1[i] = str1[i].get(i, 0) + 1
# for j in b:
#     str1[j] = str1[j].get(j, 0) + 1

# for x in str1.keys():
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")

# else:
#     print("NO")
# a = input()
# b = input()

# str1 = dict()
# str2 = dict()

# for x in a:
#     str1[x] = str1.get(x, 0) + 1
# for x in b:
#     str2[x] = str2.get(x, 0) + 1

# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break

# else:
#     print("YES")


a = input()
b = input()

str1 = dict()
str2 = dict()

for i in a:
    str1[i] = str1.get(i, 0) + 1 # 딕셔너리의 갯수를 세는 방법
for i in b:
    str2[i] = str2.get(i, 0) + 1

for x in str1.keys():
    if x in str2.keys():
        if str1[x] != str2[x]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")