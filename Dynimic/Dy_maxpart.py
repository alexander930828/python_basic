
n = int(input()) 
arr = list(map(int, input().split())) #입력
arr.insert(0, 0) #인덱스를 1에 
dy = [0]*(n+1) #다이나믹할때는 저장해놓고 꺼내서 쓰는 그런 느낌으로
dy[1] = 1 #첫번째 인덱스는 답을 넣어주고
res = 0 #가장 많은 답

for i in range(2, n+1): #전 어레이를 순회
    max = 0 #최대값을 기록
    for j in range(i-1, 0, -1): #바로 앞에있는 값부터 처음수까지 순회
        if arr[j] < arr[i] and dy[j] > max: #수열을 돌면서 뒤에 값이 앞에 있는 값들 보다 크고 / 다이나믹 즉 순열의 최대길이가 지금까지 측정해왔던 최댓값 보다 크다면 
            max = dy[j] #최대값은 지금 탐색하는 값 이전의 값들 중에서 최대값을 저장 
    dy[i] = max+1 #그리고 현재 값에는 +1한 값이 최대
    if dy[i]>res: #만약/
        res=dy[i]
print(res)


# n = int(input())
# arr = list(map(int, input().split()))
# arr.insert(0, 0)
# dy = [0]*(n+1)
# dy[1] = 1


# for i in range(2, n+1):
#     max = 0 
#     for j in range(i-1, 0, -1):
#         if arr[i]>arr[j] and dy[j]>max:
#             max = dy[j] #j중에서 가장 큰 값을 골라내고
#     dy[i] = max+1 #그 다음에 업데이트

# b=max(dy)
# print(b)