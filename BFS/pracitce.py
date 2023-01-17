from collections import deque

Q = deque()

Q.append((1, 2))

a = Q.popleft()

print(a[1])

