import sys
from collections import deque

def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:queue.append((i, j, 0))


while queue:
    x, y, d = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            queue.append((nx, ny, d + 1))

# res = all(all(cell != 0 for cell in row) for row in box)
print(d if all(all(cell != 0 for cell in row) for row in arr) else -1)