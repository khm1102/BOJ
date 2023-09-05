calculate_distance = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
find_triangle_max_diff = lambda ax, ay, bx, by, cx, cy: -1.0 if ((ax - bx) * (ay - cy) == (ay - by) * (ax - cx)) else 2 * (max(
    [calculate_distance(ax, ay, bx, by) + calculate_distance(ax, ay, cx, cy),
     calculate_distance(ax, ay, bx, by) + calculate_distance(bx, by, cx, cy),
     calculate_distance(ax, ay, cx, cy) + calculate_distance(bx, by, cx, cy)]) - min(
    [calculate_distance(ax, ay, bx, by) + calculate_distance(ax, ay, cx, cy),
     calculate_distance(ax, ay, bx, by) + calculate_distance(bx, by, cx, cy),
     calculate_distance(ax, ay, cx, cy) + calculate_distance(bx, by, cx, cy)]))
ax, ay, bx, by, cx, cy = map(int, input().split())
print(find_triangle_max_diff(ax, ay, bx, by, cx, cy))