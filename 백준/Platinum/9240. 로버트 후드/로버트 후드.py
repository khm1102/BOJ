import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def convex_hull(points):
    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    points.sort() 

    upper_hull = []
    lower_hull = []

    for point in points:
        while len(upper_hull) >= 2 and ccw(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        while len(lower_hull) >= 2 and ccw(lower_hull[-2], lower_hull[-1], point) >= 0:
            lower_hull.pop()
        upper_hull.append(point)
        lower_hull.append(point)

    return upper_hull + lower_hull[1:-1]

C = int(input())
arrows = []
for _ in range(C):
    x, y = map(int, input().split())
    arrows.append((x, y))

convex_points = convex_hull(arrows)

max_distance = 0
n = len(convex_points)

for i in range(n):
    for j in range(i + 1, n):
        max_distance = max(max_distance, distance(convex_points[i], convex_points[j]))

print(max_distance)
