a = input()
b = input()

str1 = [0]*52
str2 = [0]*52

for x in a:
    if x.isupper():
        str1[ord(x)]