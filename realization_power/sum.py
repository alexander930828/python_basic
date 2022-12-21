# n = int(input()) 
# a = list(map(int, input().split()))

# def digit_sum(x): #각 자릿수를 더하는 알고리즘 
#     sum=0 #총 합을 나타내는 수
#     while x>0: # while 문을 통하여 처음에 10으로 나눈 나머지 수를 더해줌 
#         sum+=x%10
#         x=x//10 # 10으로 다시 몫을 나눠주면 뒷에서 한자리를 빼게 됨 
#     return sum # 함수에서는 항상 리턴 값을 만들어주자 

# max = -2147000000 # 가장작은 수를 놔두고 
# for x in a: # 입력받은 값들 사이를 차례대로 호출한다 
#     tot=digit_sum(x)
#     if tot>max: # 만약 값이 더 크다면 업데이트 해준다 .
#         max=tot
#         res=x # 그리고 그 큰 값의 수를 업데이트 해준다. 

# print(res)


n = int(input())
a = list(map(int, input().split()))
maxnum = -2147000000

def digit_sum(x):
    sum=0
    while x>0:
        sum += x%10
        x = x//10
    return sum

for i in a:
    tot = digit_sum(i)
    if tot > maxnum:
        max = tot
        res = i

print(res)