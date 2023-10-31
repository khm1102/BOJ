from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
v = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    v[0][0][0] = 1

    while queue:
        y, x, breakingWall = queue.popleft()

        if y == n - 1 and x == m - 1:
            return v[y][x][breakingWall]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if (arr[ny][nx] == 0 and not v[ny][nx][breakingWall]) or (breakingWall == 0 and arr[ny][nx] == 1 and not v[ny][nx][1]): v[ny][nx][breakingWall if arr[ny][nx] == 0 else 1] = v[y][x][breakingWall] + 1; queue.append((ny, nx, breakingWall if arr[ny][nx] == 0 else 1))
    return -1

print(bfs())

