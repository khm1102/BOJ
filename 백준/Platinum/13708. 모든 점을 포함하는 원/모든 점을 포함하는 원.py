import math

coords = []
size = int(input())

for _ in range(size):
    x, y = map(int, input().split())
    coords.append((x, y))

x_avg = sum(pt[0] for pt in coords) / size
y_avg = sum(pt[1] for pt in coords) / size

prec = 0.1
max_dist = 0
for _ in range(25000):
    idx = 0
    max_dist = (x_avg - coords[0][0]) ** 2 + (y_avg - coords[0][1]) ** 2
    for j in range(1, size):
        dist = (x_avg - coords[j][0]) ** 2 + (y_avg - coords[j][1]) ** 2
        if max_dist < dist:
            max_dist = dist
            idx = j
    x_avg += (coords[idx][0] - x_avg) * prec
    y_avg += (coords[idx][1] - y_avg) * prec
    prec *= 0.999

dist = round(math.sqrt(max_dist) * 2, 2)
print('{:.2f}'.format(dist))