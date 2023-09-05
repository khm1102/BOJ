from typing import Tuple

Point = Tuple[float, float]


def CCW(a: Point, b: Point, c: Point) -> int:
    result = (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])
    return 0 if result == 0 else 1 if result > 0 else -1


def findPoint(a: Point, b: Point, c: Point, d: Point) -> Point:
    px = (a[0] * b[1] - a[1] * b[0]) * (c[0] - d[0]) - (a[0] - b[0]) * (c[0] * d[1] - c[1] * d[0])
    py = (a[0] * b[1] - a[1] * b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] * d[1] - c[1] * d[0])
    p = (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0])

    if p == 0:
        if b == c and a <= c:
            return b
        elif a == d and c <= a:
            return a
        return None

    x = px / p
    y = py / p

    return x, y


L1 = list(map(float, input().split()))
L2 = list(map(float, input().split()))

a = (L1[0], L1[1])
b = (L1[2], L1[3])
c = (L2[0], L2[1])
d = (L2[2], L2[3])

ccwValue = [CCW(a, b, c) * CCW(a, b, d), CCW(c, d, a) * CCW(c, d, b)]

if ccwValue[0] == 0 and ccwValue[1] == 0:
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c

    if a <= d and b >= c:
        print(1)
        point = findPoint(a, b, c, d)
        if point:
            print(point[0], point[1])
    else:
        print(0)
elif ccwValue[0] <= 0 and ccwValue[1] <= 0:
    print(1)
    point = findPoint(a, b, c, d)
    if point:
        print(point[0], point[1])
else:
    print(0)
