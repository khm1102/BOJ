import sys
from collections import deque

def input(): return sys.stdin.readline().strip()
def print(w):return sys.stdout.write(f"{str(w)}\n")
def bfs(graph, visited, y, x):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(y, x)])
    visited[y][x] = True
    count = 1

    while queue:
        current_y, current_x = queue.popleft()

        for dy, dx in dirs:
            ny, nx = current_y + dy, current_x + dx
            if 0 <= ny < len(graph) and 0 <= nx < len(graph) and graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
                count += 1

    return count

def f(graph):
    n = len(graph)
    visited = [[False for _ in range(n)] for _ in range(n)]
    comps = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                comps.append(bfs(graph, visited, i, j))
    return comps

graph = [list(map(int, input().strip())) for _ in range(int(input()))]

res = f(graph)
res.sort()

print(len(res))
# for count in complexes:
#     print(count)
print("\n".join(map(str, res)))
