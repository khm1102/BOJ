def solve(n, pos):
    def dfs(v):
        stack = [v]
        while stack:
            node = stack.pop()
            if visited[node] == 1:  
                return node
            if visited[node] == 0:
                visited[node] = 1
                if pos[node] == 'E':
                    next_node = node + 1
                else:
                    next_node = node - 1
                stack.append(next_node)
        return None

    visited = [0] * n
    set_pos = set()

    for i in range(n):
        if visited[i] == 0:
            start = dfs(i)
            if start is not None:
                set_pos.add(start)
            for j in range(n):
                if visited[j] == 1:
                    visited[j] = 2

    return len(set_pos)

n = int(input().strip())
pos = input().strip()

print(solve(n, pos))
