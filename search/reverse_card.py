# card = list(range(21))

# for _ in range(10):
#     s, e = map(int, input().split())
#     for j in range((e-s+1)//2):
#         card[s+j], card[e-j] = card[e-j], card[s+j]

# card.pop(0)

# print(card)

card = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2): # 팰린드롬이랑 유사하다.
        card[a+i], card[b-i] = card[b-i], card[a+i]

card.pop(0)
for j in card:
    print(j, end=' ')