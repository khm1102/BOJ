dist = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
solve = lambda ax, ay, bx, by, cx, cy: -1.0 if ((ax - bx) * (ay - cy) == (ay - by) * (ax - cx)) else 2 * (max(
    [dist(ax, ay, bx, by) + dist(ax, ay, cx, cy),
     dist(ax, ay, bx, by) + dist(bx, by, cx, cy),
     dist(ax, ay, cx, cy) + dist(bx, by, cx, cy)]) - min(
    [dist(ax, ay, bx, by) + dist(ax, ay, cx, cy),
     dist(ax, ay, bx, by) + dist(bx, by, cx, cy),
     dist(ax, ay, cx, cy) + dist(bx, by, cx, cy)]))
ax, ay, bx, by, cx, cy = map(int, input().split())
print(solve(ax, ay, bx, by, cx, cy))