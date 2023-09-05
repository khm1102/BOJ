import math
from operator import itemgetter

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2

def compare_y(a):
    return a.y

def search_all(v, s, e):
    minDist = float('inf')

    for i in range(s, e + 1):
        for j in range(i + 1, e + 1):
            dist = distance(v[i], v[j])
            minDist = min(minDist, dist)

    return minDist

def search_point(v, start, end):
    count = end - start + 1

    if count <= 3:
        return search_all(v, start, end)
    
    mid = (start + end) // 2
    left = search_point(v, start, mid)
    right = search_point(v, mid + 1, end)

    answer = min(left, right)

    final = [i for i in v[start:end+1] if (i.x - v[mid].x)**2 < answer]
    final.sort(key=compare_y)

    maxIndex = len(final)

    for i in range(maxIndex - 1):
        for j in range(i + 1, maxIndex):
            y = final[j].y - final[i].y

            if y*y < answer:
                dist = distance(final[j], final[i])
                answer = min(dist, answer)
            else:
                break

    return answer

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

points.sort(key=lambda p: (p.x, p.y))

answer = search_point(points, 0, n-1)

print(answer)
    