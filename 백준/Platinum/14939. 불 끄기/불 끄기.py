M = 10
INF = float('inf')

arr = [[False for _ in range(15)] for _ in range(15)]
tmp = [[False for _ in range(15)] for _ in range(15)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = INF

def outrange(x, y):
    return x < 0 or x >= M or y < 0 or y >= M

def toggle(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not outrange(nx, ny):
            tmp[nx][ny] = not tmp[nx][ny]
    tmp[x][y] = not tmp[x][y]

def init():
    for i in range(M):
        for j in range(M):
            tmp[i][j] = arr[i][j]

def islight():
    return any(any(row) for row in tmp)

for i in range(M):
    row = input().strip()
    for j in range(M):
        if row[j] == 'O':
            arr[i][j] = True

for step in range(1 << M):
    cnt = 0
    init()

    for bit in range(M):
        if step & (1 << bit):
            cnt += 1
            toggle(0, bit)

    for x in range(1, M):
        for y in range(M):
            if tmp[x - 1][y]:
                toggle(x, y)
                cnt += 1

    if not islight():
        ans = min(cnt, ans)

if ans == INF:
    print(-1)
else:
    print(ans)
