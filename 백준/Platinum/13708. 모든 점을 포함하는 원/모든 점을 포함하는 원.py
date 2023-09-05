import math

coordinates = []

size = int(input())

for _ in range(size):
    x, y = map(int, input().split())
    coordinates.append((x, y))

x_avg = sum(pt[0] for pt in coordinates) / size
y_avg = sum(pt[1] for pt in coordinates) / size

precision = 0.1
max_distance = 0
for _ in range(25000):
    idx = 0
    max_distance = (x_avg - coordinates[0][0]) ** 2 + (y_avg - coordinates[0][1]) ** 2
    for j in range(1, size):
        distance = (x_avg - coordinates[j][0]) ** 2 + (y_avg - coordinates[j][1]) ** 2
        if max_distance < distance:
            max_distance = distance
            idx = j
    x_avg += (coordinates[idx][0] - x_avg) * precision
    y_avg += (coordinates[idx][1] - y_avg) * precision
    precision *= 0.999

distance = round(math.sqrt(max_distance) * 2, 2)

print('{:.2f}'.format(distance))
