# 익명의 함수 또는 람다 표현식

# def plus_one(x):
#     return x+1

# print(plus_one(1))

# plus_two=lambda x: x+2

# print(plus_two(1))

#내장함수의 인자로 쓸 때 편리하다.

def plus_one(x):
    return x+1

a=[1, 2, 3]

print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))

