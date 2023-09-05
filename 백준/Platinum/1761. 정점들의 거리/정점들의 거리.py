import sys
from collections import deque


n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)
parent = [0] * (n + 1)
depth = [0] * (n + 1)

for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a].append((b, d))
    tree[b].append((a, d))


def bfs(root):
    queue = deque([(root, 0, 0)])

    while queue:
        node, d, p = queue.popleft()
        depth[node] = d
        parent[node] = p

        for child, dist_child in tree[node]:
            if child != p:
                dist[child] = dist[node] + dist_child
                queue.append((child, d + 1, node))


def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    while depth[u] != depth[v]:
        u = parent[u]


    while u != v:
        u = parent[u]
        v = parent[v]

    return u

bfs(1)


m = int(sys.stdin.readline())
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    lca_node = lca(u, v)
    distance = dist[u] + dist[v] - 2 * dist[lca_node]
    print(distance)
