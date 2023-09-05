def GCD(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def INV(a, m):
    m0 = m
    y, x = 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x

def f(a, b, s):
    if a == 0:
        if b == 0:
            if s == 0:
                return "YES"
            else:
                return "NO"
        if s % b == 0:
            return "YES"
        else:
            return "NO"

    if b == 0:
        if s % a == 0:
            return "YES"
        else:
            return "NO"
    else:
        g = GCD(a, b)
        if s % g != 0:
            return "NO"
        if g > 1:
            return f(a // g, b // g, s // g)
        else:
            c = INV(a, b)
            x = (c * s) % b
            y = (s - a * x) // b
            if y < 0:
                return "NO"
            while GCD(x, y) != 1 and y >= 0:
                x += b
                y -= a
            assert a * x + b * y == s
            if y < 0:
                return "NO"
            else:
                return "YES"
a, b, s = map(int, input().split())
result = f(a, b, s)
print(result)