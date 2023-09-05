import math

class Point:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx

points = []
ansX = []
ansY = []

def compare(p1, p2):
    if p1.x < p2.x:
        return True
    elif p1.x == p2.x:
        if p1.y < p2.y:
            return True
        return False
    return False

def absolute(d):
    if d > 0.0:
        return d
    else:
        return -d

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    p = Point(x, y, i+1)
    points.append(p)

points = sorted(points, key=lambda p: (p.x, p.y))

mx = -1
a, b = 0, 0
idxAnsX, idxAnsY = 0, 0


for i in range(n-1):
    if mx < absolute((points[i].y - points[i+1].y) / (points[i].x - points[i+1].x)):
        mx = absolute((points[i].y - points[i+1].y) / (points[i].x - points[i+1].x))

for i in range(n-1):
    if mx == absolute((points[i].y - points[i+1].y) / (points[i].x - points[i+1].x)):
        ansX.append(points[i].idx)
        ansY.append(points[i+1].idx)
        idxAnsX += 1
        idxAnsY += 1

ansX = sorted(ansX)
ansY = sorted(ansY)

a = ansX[0] if ansX[0] < ansY[0] else ansY[0]
b = ansY[0] if ansX[0] < ansY[0] else ansX[0]

print(a, b)
