from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
target = []
v = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            target.append((j, i))
            arr[i][j] = '.'
            v.append((j, i))
        elif arr[i][j] == '.':
            v.append((j, i))

q = deque()
ans = 0
q.append(target[0])
visited[target[0][1]][target[0][0]] = True

while True:
    next = deque()
    while q:
        c, r = q.popleft()
        for i in range(4):
            nx = dx[i] + c
            ny = dy[i] + r
            if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx]:
                if target[1] == (nx, ny):
                    print(ans)
                    exit()
                elif arr[ny][nx] == 'X':
                    next.append((nx, ny))
                else:
                    q.append((nx, ny))
                visited[ny][nx] = True
    q = next
    ans += 1

    n = len(v)
    for _ in range(n):
        c, r = v.popleft()
        for j in range(4):
            nx = dx[j] + c
            ny = dy[j] + r
            if 0 <= nx < C and 0 <= ny < R and arr[ny][nx] == 'X':
                v.append((nx, ny))
                arr[ny][nx] = '.'
