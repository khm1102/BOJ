def linear_regression(n, points):
    S_x = 0
    S_y = 0
    S_xx = 0
    S_xy = 0

    for x, y in points:
        S_x += x
        S_y += y
        S_xx += x ** 2
        S_xy += x * y

    numerator_a = n * S_xy - S_x * S_y
    denominator_a = n * S_xx - S_x ** 2

    if denominator_a != 0:
        a_2 = numerator_a / denominator_a
        b_2 = (S_y - a_2 * S_x) / n
        return a_2, b_2
    else:
        return None

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

result = linear_regression(n, points)

if result:
    a_2, b_2 = result
    print(f"{a_2:.10f} {b_2:.10f}")
else:
    print("EZPZ")
