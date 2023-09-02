N = int(input())
r = 2
n = 3
tmp = 1
f = False

while r <= 1000000:
    tmp = r * r * r
    n = 3
    while n <= 40:
        if (N * (r - 1)) % (tmp - 1) == 0:
            f = True
            break
        if tmp > 1e12:
            break
        tmp *= r
        n += 1
    if f:
        break
    r += 1

if not f:print(-1)
else:
    print(n)
    a = N * (r - 1) // (tmp - 1)
    print(*[a * r**i for i in range(n)])
