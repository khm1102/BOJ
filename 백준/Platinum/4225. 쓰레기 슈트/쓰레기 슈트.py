from functools import cmp_to_key
import math


def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

def cmp(a, b):
    return 1 if ccw(temp, a, b) < 0 else -1


def convex_hull(points):
    stk = points[:2]
    for point in points[2:]:
        while len(stk) > 1 and ccw(stk[-2], stk[-1], point) < 0:
            stk.pop()
        stk.append(point)
    return stk


def dist(target, p0, p1):
    if p0[0] == p1[0]:
        return abs(target[0] - p0[0])
    if p0[1] == p1[1]:
        return abs(target[1] - p0[1])

    a, b = (p1[1] - p0[1]) / (p1[0] - p0[0]), -1
    c = -a * p0[0] + p0[1]
    return abs(a * target[0] + b * target[1] + c) / math.sqrt(a ** 2 + b ** 2)


def solve(idx):
    global temp
    N = int(input())
    if N == 0:
        return False

    points = [list(map(int, input().split())) for _ in range(N)]
    temp, *points = sorted(points)
    points.sort(key=cmp_to_key(cmp))

    hull = convex_hull([temp] + points)
    length = len(hull)

    ans = float('inf')
    for i in range(length):
        k = (i + 1) % length
        tmp = 0.
        for j in range(length):
            tmp = max(tmp, dist(hull[j], hull[i], hull[k]))
        ans = min(ans, tmp)

    print(f'Case {idx}: {math.ceil(ans * 100) / 100.0:.2f}')
    return True


idx = 1
while solve(idx):
    idx += 1
