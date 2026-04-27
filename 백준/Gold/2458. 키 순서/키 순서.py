def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        for i in graph.get(node, []):
            if i not in visited:
                stack.append(i)

    return len(visited) - 1


n, m = map(int, input().split())
fwd, bwd = {}, {}

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    fwd.setdefault(a, []).append(b)
    bwd.setdefault(b, []).append(a)

print(sum(dfs(bwd, i) + dfs(fwd, i) == n - 1 for i in range(n)))
