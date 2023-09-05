from collections import defaultdict

def solve():
    N = int(input().strip())
    points = []
    for _ in range(N):
        x, y = map(int, input().strip().split())
        points.append((x, y))

    if N < 3:
        print(-1)
        return

    max_points = 0
    for i in range(N):
        slopes = defaultdict(int)
        for j in range(N):
            if i != j:
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0:
                    slope = float('inf')
                else:
                    slope = dy / dx
                slopes[slope] += 1
        max_points = max(max_points, max(slopes.values()) + 1)
    
    if max_points < 3:
        print(-1)
    else:
        print(max_points)

solve()
