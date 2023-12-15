m = int(input())
k = int(input())
c = list(map(int, input().split()))

d = [-1] * 10000
for i in range(5000):
    idx = i
    if idx < 0:
        d[idx] = -1
    elif idx == 0:
        d[idx] = 0
    elif d[idx] == -1:
        r = 0
        for j in range(k):
            t = d[idx - c[j]]
            if t == -1:
                continue
            elif t == 0:
                r = 1
                break
        d[idx] = r

cs = 1
for i in range(100, 2000):
    for j in range(1001, 1001 + i):
        if d[j] != d[j + i]:
            break
    else:
        cs = i
        break

res = 0
if m > 1000:
    for i in range(1, 1001):
        if d[i] == 0:
            res += 1

    count = 0
    for i in range(1001, 1001 + cs):
        if d[i] == 0:
            count += 1

    res += ((m - 1000) // cs) * count

    for i in range(1001, 1001 + ((m - 1000) % cs)):
        if d[i] == 0:
            res += 1
else:
    for i in range(1, m + 1):
        if d[i] == 0:
            res += 1

print(res)
