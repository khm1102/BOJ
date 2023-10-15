import sys
from collections import deque

def input(): return sys.stdin.readline().strip()
def print(val): return sys.stdout.write(str(val))

def bfs(maze, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0))
    v = [[False] * m for _ in range(n)]
    v[0][0] = True
    dist = [[0] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not v[nx][ny]:
                v[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist[n - 1][m - 1] + 1
def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    print(bfs(arr, n, m))

if __name__ == "__main__":
    main()