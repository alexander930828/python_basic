# n, m = map(int, input().split())

# cnt = [0]*100

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         cnt[i+j]+=1

# print(cnt)

# n, m = map(int, input().split()) 
# cnt = [0]*(n+m+3)
# max = 0

# for i in range(1, n+1): # n+1 까지 하나 하나 탐색을 하면서 
#     for j in range(1, m+1):
#         cnt[i+j]+=1 # 주사위의 합이 되는 곳에다가 카운팅을 더 해준다. 몇번이나 나오는지 

# for i in range(n+m+1): #카운팅이 가장 최대로 가지는 값을 max =0 에서 차례대로 수를 비교하여 큰 값이 나오면 그 값으로 업데이트 시켜준다. 그러면 최대값 즉 주사위를 던졌을 때 가장 많은 경우의 수를 알 수 있음
#     if cnt[i]>max: 
#         max=cnt[i] # 가장 많이 나온 곳은 얼마의 카운팅이 되어있는지 = 얼마나 출현하는지

# for i in range(n+m+1):
#     if cnt[i]==max: # 처음부터 끝까지 순회하면서 최대로 나온 갯수와 같은게 있다면 그 인덱스를 출력하는 것 
#         print(i, end=' ') 


n, m = map(int, input().split())
cnt = [0]*(n+m+3)
maxnum = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

for i in range(n+m+3):
    if cnt[i] > maxnum:
        maxnum = cnt[i]

for i in range(n+m+3):
    if cnt[i] == maxnum:
        print(i, end=' ')