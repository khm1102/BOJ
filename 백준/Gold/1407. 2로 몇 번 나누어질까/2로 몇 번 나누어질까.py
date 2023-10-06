def f(x):
    value = 0
    i = 1
    while x > 0:
        y = (x + 1) // 2
        value += y * i
        x //= 2
        i *= 2
    return value
a, b = map(int, input().split())
print(f(b) - f(a - 1))