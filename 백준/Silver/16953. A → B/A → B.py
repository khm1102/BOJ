from collections import deque

def optimized_bfs(a, b):
    if a == b:
        return 0

    visited = set()
    q = deque([(a, 1)])

    while q:
        n, t = q.popleft()
        if n in visited or n > b:
            continue

        visited.add(n)

        if n == b:
            return t

        q.append((n * 2, t + 1))
        q.append((int(str(n) + "1"), t + 1))

    return -1

a, b = map(int, input().split())
result = optimized_bfs(a, b)
print(result)
