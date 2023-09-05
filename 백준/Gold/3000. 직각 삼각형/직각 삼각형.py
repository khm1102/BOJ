from collections import defaultdict

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

x_count = defaultdict(int)
y_count = defaultdict(int)

for point in points:
    x, y = point
    x_count[x] += 1
    y_count[y] += 1

result = 0
for point in points:
    x, y = point
    x_value = x_count[x] - 1
    y_value = y_count[y] - 1
    result += x_value * y_value

print(result)
