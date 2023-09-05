p = []
n = int(input())
n //= 2

to = [0, 0, 2, 3, 1]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    a = to[a]
    c = to[c]
    x = a * 51 + b
    y = c * 51 + d
    if a > 1:
        x += 51 - 2 * b
    if c > 1:
        y += 51 - 2 * d

    p.append((min(x, y), max(x, y)))

ans = 0
cross = [0] * 55

for i in range(n):
    a, b = p[i]
    for j in range(n):
        c, d = p[j]
        if a < c and c < b and b < d:
            ans += 1
            cross[i] += 1
            cross[j] += 1

print(ans)
print(max(cross[:n]))
