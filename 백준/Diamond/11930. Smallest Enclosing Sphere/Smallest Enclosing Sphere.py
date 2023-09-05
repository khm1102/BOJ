import math

n = int(input())
v = []
x, y, z = 0, 0, 0

for _ in range(n):
    a, b, c = map(float, input().split())
    x += a
    y += b
    z += c
    v.append((a, b, c))

x /= n
y /= n
z /= n

ratio = 0.1
ans = 0

for _ in range(20000):
    idx = -1
    ans = 0

    for i in range(n):
        a, b, c = v[i]
        dist = (x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2

        if ans < dist:
            idx = i
            ans = dist

    a, b, c = v[idx]
    x += (a - x) * ratio
    y += (b - y) * ratio
    z += (c - z) * ratio
    ratio *= 0.999

print("{:.2f}".format(math.sqrt(ans)))
