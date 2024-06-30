from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
visited = [[False] * n for _ in range(n)]
queue = deque([(r1, c1, 0)])
visited[r1][c1] = True

result = -1
while queue:
    r, c, dist = queue.popleft()

    if (r, c) == (r2, c2):
        result = dist
        break

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            visited[nr][nc] = True
            queue.append((nr, nc, dist + 1))

print(result)
