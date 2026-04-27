from collections import deque

def solve(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if not visited[i]:
                cnt_arr[i] += 1
                visited[i] = True
                queue.append(i)

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
cnt_arr = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

max_value = 0
result = []

for i in range(1, N + 1):
    solve(i)
    max_value = max(max_value, max(cnt_arr))

result = [i for i, cnt in enumerate(cnt_arr) if cnt == max_value]
print(*result)
