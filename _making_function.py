# def add(a, b):
#     c=a+b
#     print(c)

# add(3, 2)
# add(5, 7)

# 특정 작업을 반복해야 될 때가 있다. 

# def add(a, b):
#     c=a+b
#     return c

# # return은 함수가 종료되는 것도 있다.     

# x=add(3, 2)
# print(x)

def add(a, b):
    c=a+b
    d=a-b
    return c, d

print(add(3, 2))

