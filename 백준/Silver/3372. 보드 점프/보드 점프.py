n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or arr[i][j] == 0:
            continue
        jump = arr[i][j]
        if i + jump < n:
            dp[i + jump][j] += dp[i][j]
        if j + jump < n:
            dp[i][j + jump] += dp[i][j]

print(dp[n-1][n-1])
