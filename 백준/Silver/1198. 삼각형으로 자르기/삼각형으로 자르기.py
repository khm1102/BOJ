def get_area(a, b, c, points):
    return abs((points[a][1] - points[b][1]) * (points[c][0] - points[b][0]) - (points[a][0] - points[b][0]) * (points[c][1] - points[b][1]))
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            ans = max(ans, get_area(i, j, k, points))
print(ans / 2)