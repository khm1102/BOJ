n, m, k = map(int, input().split())
dp = [[0] * 1005 for _ in range(1005)]
maps = [[0] * 1005 for _ in range(1005)]

for i in range(1, n + 1):
    maps[i][1:m + 1] = map(int, input().split())

dp[1][1] = k - 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        d = dp[i][j]
        dp[i][j + 1] += (d // 2 + (d % 2) * maps[i][j])
        dp[i + 1][j] += (d // 2 + (d % 2) * (not maps[i][j]))

r, c = 1, 1
while r <= n and c <= m:
    if (dp[r][c] % 2) ^ maps[r][c]:
        c += 1
    else:
        r += 1

print(r, c)
