
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a) 

max_computers = 0
result_node = []

for start_node in range(1, n + 1):
    visited = [False] * (n + 1)
    result = 0
    
    stack = [start_node]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result += 1
            stack.extend(graph[node])
    
    if result > max_computers:
        max_computers = result
        result_node = [start_node]
    elif result == max_computers:
        result_node.append(start_node)

result_node.sort()
print(' '.join(map(str, result_node)))

