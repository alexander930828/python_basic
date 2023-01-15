import itertools as it

n = 5
a = list(range(1, n+1))

for tmp in it.permutations(a, 3):
    print(tmp)