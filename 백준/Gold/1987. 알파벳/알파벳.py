def dfs(x, y, path):
    global max_path
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_path = max(max_path, len(path))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in path:
            dfs(nx, ny, path + board[nx][ny])

R, C = map(int, input().split())
board = [input() for _ in range(R)]
max_path = 0
dfs(0, 0, board[0][0])
print(max_path)
