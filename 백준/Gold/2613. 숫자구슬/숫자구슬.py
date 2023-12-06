def f(v):
    c = 1
    s = 0

    for i in range(n):
        if m[i] > v:
            return False

        if s + m[i] <= v:
            s += m[i]
        else:
            c += 1
            s = m[i]

    return c <= k


n, k = map(int, input().split())
m = list(map(int, input().split()))

l, r = 1, n * 100

while l <= r:
    mid = (l + r) // 2
    if f(mid):
        r = mid - 1
    else:
        l = mid + 1

print(l)

c, s, g = 0, 0, 1
a = []
for i in range(n):
    s += m[i]
    if s > l:
        a.append(c)
        s = m[i]
        c = 0
        g += 1
    c += 1

a.append(c)
pos = len(a) - 1

while g < k:
    if a[pos] == 1:
        pos -= 1
    else:
        a[pos] -= 1
        a.append(1)
        g += 1

print(*a)
