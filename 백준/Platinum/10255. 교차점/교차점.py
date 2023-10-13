import sys

def input(): return sys.stdin.readline().strip()

def f(x1, y1, x2, y2, x3, y3):
    a = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def g(x1, y1, x2, y2, x3, y3, x4, y4):
    if f(x1, y1, x2, y2, x3, y3) * f(x1, y1, x2, y2, x4, y4) <= 0 and f(x3, y3, x4, y4, x1, y1) * f(x3, y3, x4, y4, x2, y2) <= 0:
        if (x1 > x3 and x1 > x4 and x2 > x3 and x2 > x4) or (x3 > x1 and x3 > x2 and x4 > x1 and x4 > x2):
            return False
        elif (y1 > y3 and y1 > y4 and y2 > y3 and y2 > y4) or (y3 > y1 and y3 > y2 and y4 > y1 and y4 > y2):
            return False
        else:
            return True
    else:
        return False

def l(x1, y1, x2, y2, a, b, c, d):
    if a == c and (a == x1 or a == x2) and ((b < y2 and d > y1) or (d < y2 and b > y1)):
        return True
    elif b == d and (b == y1 or b == y2) and ((a < x2 and c > x1) or (c < x2 and a > x1)):
        return True
    return False

def p(x1, y1, x2, y2, x3, y3, x4, y4):
    if f(x1, y1, x2, y2, x3, y3) * f(x1, y1, x2, y2, x4, y4) == 0 and f(x3, y3, x4, y4, x1, y1) * f(x3, y3, x4, y4, x2, y2) <= 0:
        return True
    else:
        return False

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    a, b, c, d = map(int, input().split())
    x = 0
    if g(a, b, c, d, x1, y1, x1, y2):
        x += 1
    if g(a, b, c, d, x1, y2, x2, y2):
        x += 1
    if g(a, b, c, d, x2, y2, x2, y1):
        x += 1
    if g(a, b, c, d, x2, y1, x1, y1):
        x += 1
    if l(x1, y1, x2, y2, a, b, c, d):
        print(4)
    else:
        if p(a, b, c, d, x1, y1, x1, y2):
            x -= 0.5
        if p(a, b, c, d, x1, y2, x2, y2):
            x -= 0.5
        if p(a, b, c, d, x2, y2, x2, y1):
            x -= 0.5
        if p(a, b, c, d, x2, y1, x1, y1):
            x -= 0.5
        print(int(x))
