def f(n):
    if n == 0:return 0
    elif n == 1:return 1

    a, b = 0, 1
    for _ in range(abs(n) - 1):a, b = b, (a + b) % 1000000000

    if n < 0 and n % 2 == 0:return -b
    else:return b

res = f(int(input()))

if res > 0:print(1)
elif res == 0:print(0)
else:print(-1)

print(abs(res) % 1000000000)