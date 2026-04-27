n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [float('inf')] * (k + 1)
dp[0] = 0

for i in arr:
    for j in range(i, k + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)

print(-1 if dp[k] == float('inf') else dp[k])
