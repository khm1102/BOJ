import math

# 두 점 사이의 거리
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_planets(x1, y1, x2, y2, planets):
    count = 0
    for cx, cy, r in planets:
        if distance(x1, y1, cx, cy) < r and distance(x2, y2, cx, cy) < r and distance(x1, y1, x2, y2) > 2 * r:
            count += 1
        elif (distance(x1, y1, cx, cy) < r and distance(x2, y2, cx, cy) > r) or (distance(x1, y1, cx, cy) > r and distance(x2, y2, cx, cy) < r):
            count += 1
    return count
t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [tuple(map(int, input().split())) for _ in range(n)]
    print(get_planets(x1, y1, x2, y2, planets))
