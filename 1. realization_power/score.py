# # 최솟값 구하기

# arr=[5, 3, 7, 9, 2, 5, 2, 6]
# arrmin=float('inf')

# for i in range(len(arr)):
#     if arr[i]<arrmin:
#         arrmin=arr[i]

# n=int(input())
# a=list(map(int, input().split()))

# arrmin=float('inf')
# mean=sum(a)/len(a)

# for i in range(a):
#     if abs(a[i]- mean) < arrmin:


# n=int(input())
# a=list(map(int, input().split()))
# ave=round(sum(a)/n)
# min=2147000000

# for idx, x in enumerate(a):
#     tmp=abs(x-ave)
#     if tmp<min:
#         min=tmp
#         score=x
#         res=idx+1
#     elif tmp==min:
#         if x>score:
#             score=x
#             res=idx+1


n=int(input())
a=list(map(int, input().split()))
avg=int(sum(a)/len(a)+0.5)
min=2147000000

for idx, x in enumerate(a): # 점수와 순서(인덱스)를 모두 기억해야하는 경우에 사용
    tmp=abs(x-avg) # 평균
    if tmp < min: # 만약 스코어에서 평균을 뺀 절댓값이 최솟값보다 작다면 
        min=tmp #거리가 짧은 것으로 업데이트 시켜주고
        score=x #점수를 기록한다.
        res=idx+1 #몇번째 학생인지도 기록한다.
    elif tmp == min:
        if x>score: #이번에 들어온 값의 점수가 크다면 
            score=x #업데이트 
            res=idx+1 #인덱스 값도 기록 

print(score, res)
