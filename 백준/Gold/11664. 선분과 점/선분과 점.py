import math

ax, ay, az, bx, by, bz, cx, cy, cz = map(float, input().split())

for i in range(1000000):
    x1 = ax + (bx - ax) / 3
    x2 = ax + 2 * (bx - ax) / 3
    y1 = ay + (by - ay) / 3
    y2 = ay + 2 * (by - ay) / 3
    z1 = az + (bz - az) / 3
    z2 = az + 2 * (bz - az) / 3

    mid1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 + (z1 - cz) ** 2
    mid2 = (x2 - cx) ** 2 + (y2 - cy) ** 2 + (z2 - cz) ** 2

    if mid1 < mid2:
        bx, by, bz = x2, y2, z2
    else:
        ax, ay, az = x1, y1, z1

print("{:.9f}".format(min(math.sqrt(mid1), math.sqrt(mid2))))
