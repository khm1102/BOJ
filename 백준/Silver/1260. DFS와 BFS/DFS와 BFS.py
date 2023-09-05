from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)

dfs(graph, V, visited)
print()

visited = [False] * (N + 1)

bfs(graph, V, visited)
print()
