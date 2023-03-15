a = "3141592"
b = "271"

t_slice = [a[i: i+len(b)] for i in range(0, len(a))]

print(t_slice)
n_slice = list(map(int, t_slice))
print(n_slice)