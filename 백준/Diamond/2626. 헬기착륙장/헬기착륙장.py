import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

def input_points():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    return points

def solve(points):
    norm = lambda x, y: x*x + y*y
    avg = Point()
    for point in points:
        avg.x += point.x
        avg.y += point.y
    avg.x *= 1.0 / len(points)
    avg.y *= 1.0 / len(points)
    ans = 1e10
    px, py, w = avg.x, avg.y, 0.1
    cnt = 10000
    while cnt > 0:
        max_v = 0
        max_id = 0
        for i, point in enumerate(points):
            tmp_v = norm(px - point.x, py - point.y)
            if tmp_v > max_v:
                max_v = tmp_v
                max_id = i
        if max_v < ans:
            ans = max_v
        px += (points[max_id].x - px) * w
        py += (points[max_id].y - py) * w
        w *= 0.995
        cnt -= 1
    return px, py, math.sqrt(ans)

def main():
    points = input_points()
    px, py, ans = solve(points)
    print(f"{px:.3f} {py:.3f}")
    print(f"{ans:.3f}")

if __name__ == "__main__":
    main()
