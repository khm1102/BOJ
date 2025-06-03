n, m = map(int, input().split())
grid = [input() for _ in range(n)]

max_side = 1

for i in range(n):
    for j in range(m):
        max_k = min(n - 1 - i, m - 1 - j)
        if max_k + 1 <= max_side:
            continue

        for k in range(max_k, -1, -1):
            side = k + 1
            if side <= max_side:
                break

            c = grid[i][j]
            if (grid[i][j + k] == c and
                    grid[i + k][j] == c and
                    grid[i + k][j + k] == c):
                max_side = side
                break

print(max_side * max_side)
