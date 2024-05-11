from collections import deque

def solution(n, edge):
    adj = {i: [] for i in range(1, n+1)}
    for e1, e2 in edge:
        adj[e1].append(e2)
        adj[e2].append(e1)
    
    visit = [0] * (n + 1)
    q = deque([(1, 0)]) 
    max_depth = 0
    visit[1] = 1
    
    while q:
        node, depth = q.popleft()
        for next_node in adj[node]:
            if not visit[next_node]:
                visit[next_node] = depth + 1
                q.append((next_node, depth + 1))
                max_depth = max(max_depth, depth + 1)
                
    return visit.count(max_depth)
