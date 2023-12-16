MAX = 10
INF = float('inf')

arr = [[False for _ in range(15)] for _ in range(15)]
tmp_arr = [[False for _ in range(15)] for _ in range(15)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = INF

def outrange(x, y):
    return x < 0 or x >= MAX or y < 0 or y >= MAX

def toggle(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not outrange(nx, ny):
            tmp_arr[nx][ny] = not tmp_arr[nx][ny]
    tmp_arr[x][y] = not tmp_arr[x][y]

def init():
    for i in range(MAX):
        for j in range(MAX):
            tmp_arr[i][j] = arr[i][j]

def islight():
    for i in range(MAX):
        for j in range(MAX):
            if tmp_arr[i][j]:
                return True
    return False

for i in range(MAX):
    row = input().strip()
    for j in range(MAX):
        if row[j] == 'O':
            arr[i][j] = True

for step in range(1 << MAX):
    cnt = 0
    init()

    for bit in range(MAX):
        if step & (1 << bit):
            cnt += 1
            toggle(0, bit)

    for x in range(1, MAX):
        for y in range(MAX):
            if tmp_arr[x - 1][y]:
                toggle(x, y)
                cnt += 1

    if not islight():
        ans = min(cnt, ans)

if ans == INF:
    print(-1)
else:
    print(ans)
