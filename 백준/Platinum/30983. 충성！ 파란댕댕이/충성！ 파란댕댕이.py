import sys
MOD = 1_000_000_009
input = sys.stdin.read
data = list(map(int, input().split()))
n, m, t = data[:3]
matrix = [[0] * (n * 2) for _ in range(n * 2)]
[idx := 3, [matrix[i + n].__setitem__(i, 1) for i in range(n)]]

for _ in range(m):
    cmd = data[idx]
    if cmd == 1:
        a, b = data[idx + 1] - 1, data[idx + 2] - 1
        matrix[a][b] += 1
        matrix[b][a] += 1
        idx += 3
    else:
        a, b, c = data[idx + 1] - 1, data[idx + 2] - 1, data[idx + 3] - 1
        for x, y in [(a, b), (b, a), (a, c), (c, a), (b, c), (c, b)]:
            matrix[x][y + n] += 1
        idx += 4

res = [[1 if i == j else 0 for j in range(n * 2)] for i in range(n * 2)]
while t:
    if t % 2:
        res = [[sum(res[i][k] * matrix[k][j] for k in range(n * 2)) % MOD for j in range(n * 2)] for i in range(n * 2)]
    matrix = [[sum(matrix[i][k] * matrix[k][j] for k in range(n * 2)) % MOD for j in range(n * 2)] for i in range(n * 2)]
    t //= 2

print('\n'.join(map(str, [res[i][0] for i in range(n)])))
