n = int(input())
l, r = [], []
temp_1, temp_2 = 0, n
r.append(n)
for i in range(n-1, 0, -1):
    if len(l) < len(r):
        l.append(i)
        temp_1 += i
    elif len(l) > len(r):
        r.append(i)
        temp_2 += i
    else:
        if temp_1 < temp_2:
            temp_1 += i;l.append(i)
        else:
            temp_2 += i;r.append(i)

r.reverse()
print(' '.join(map(str, l + r)))