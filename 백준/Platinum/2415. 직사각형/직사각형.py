import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, p1):
        return p1.x == self.x and p1.y == self.y


class Edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.length = 0


def cmp(e1, e2):
    if e1.length == e2.length:
        return (e1.a.x + e1.b.x) < (e2.a.x + e2.b.x)
    return e1.length < e2.length


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + 1e-5)


n = int(input())
p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append(Point(x, y))

m = 0
e = []
for i in range(1, n):
    for j in range(i):
        e.append(Edge(p[j], p[i]))
        e[m].length = (e[m].a.x - e[m].b.x) ** 2 + (e[m].a.y - e[m].b.y) ** 2
        m += 1

e.sort(key=lambda x: (x.length, x.a.x + x.b.x))

res = 0
for i in range(m):
    for j in range(i + 1, m):
        if e[i].a == e[j].a or e[i].a == e[j].b or e[i].b == e[j].a or e[i].b == e[j].b:
            continue
        if e[i].length != e[j].length or e[i].a.x + e[i].b.x != e[j].a.x + e[j].b.x:
            break
        if e[i].a.y + e[i].b.y == e[j].a.y + e[j].b.y:
            area = dist(e[j].a, e[i].a) * dist(e[j].b, e[i].a) + 1e-5
            if res < area:
                res = area

print(int(res))
