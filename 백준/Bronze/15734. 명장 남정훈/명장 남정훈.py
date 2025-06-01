l, r, a = map(int, input().split())

temp = abs(l-r)

if a <= temp:
    print((min(l,r) + a) * 2)
else:
    a -= temp
    b = max(l,r)
    print((b + a // 2) * 2)
