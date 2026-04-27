n, t = int(input()), int()
s, e = map(int, input().split())

for _ in range(n - 1):
    x, y = map(int, input().split())
    if x > e: t += e - s;s, e = x, y
    elif y > e: e = y

print(t + e -s)

