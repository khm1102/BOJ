import math

while True:
    N = int(input())

    if N == 0:
        break

    a = [0] * N
    b = [0] * N
    c = [0] * N

    for i in range(N):
        a[i], b[i], c[i] = map(float, input().split())

    x = sum(a) / N
    y = sum(b) / N
    z = sum(c) / N

    ratio = 0.1
    max_distance = 0
    current_distance = 0

    for i in range(70000):
        max_distance_index = 0
        max_distance = math.hypot(x - a[0], y - b[0], z - c[0])

        for j in range(1, N):
            current_distance = math.hypot(x - a[j], y - b[j], z - c[j])
            if max_distance < current_distance:
                max_distance = current_distance
                max_distance_index = j

        x += (a[max_distance_index] - x) * ratio
        y += (b[max_distance_index] - y) * ratio
        z += (c[max_distance_index] - z) * ratio
        ratio *= 0.999

    if round(x) == 0:
        x = 0
    if round(y) == 0:
        y = 0
    if round(z) == 0:
        z = 0

    print(f"{max_distance:.5f}")
