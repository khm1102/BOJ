a = input()
b = input()
s = 0
min_len = min(len(a), len(b))
while s < min_len and a[s] == b[s]:s += 1
e = 0
while e < min_len and a[-1 - e] == b[-1 - e]:e += 1

if s >= min_len - e:
    if len(a) > len(b):print(0)
    else:print(len(b) - len(a))
else:print(len(b) - e - s)