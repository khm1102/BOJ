# 서강대학교 Official Solutions 풀이를 바탕으로 생각함
def solve():
    N, M = map(int, input().split())
    points = [(x, y) for x in range(N + 1) for y in range(M + 1)]
    triangles = set()

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                p1, p2, p3 = points[i], points[j], points[k]
                x1, y1 = p1
                x2, y2 = p2
                x3, y3 = p3

                if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                    continue
                side1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                side2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
                side3 = (x2 - x3) ** 2 + (y2 - y3) ** 2

                triangle = tuple(sorted([side1, side2, side3]))
                triangles.add(triangle)

    print(len(triangles))
solve()
