import math

d = lambda a, b: a ** 2 + b ** 2

n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]

x = sum(point[0] for point in points) / n
y = sum(point[1] for point in points) / n

p = 0.1
for _ in range(30000):
    f = max(range(n), key=lambda j: d(x - points[j][0], y - points[j][1]))
    x += (points[f][0] - x) * p
    y += (points[f][1] - y) * p
    p *= 0.999
res = math.sqrt(d(x - points[f][0], y - points[f][1]))
print(f"{x:.10f} {y:.10f} {res:.10f}")
