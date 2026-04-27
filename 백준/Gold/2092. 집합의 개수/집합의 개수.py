MOD = 1000000

t, a, s, b = map(int, input().split())

mp = [0] * 201
dp = [[0] * 4001 for _ in range(201)]
res = 0

dp[0][0] = 1

a_values = list(map(int, input().split()))
for x in a_values:
    mp[x] += 1

for i in range(1, t + 1):
    for k in range(mp[i] + 1):
        dp[i][k] = 1

    for j in range(a + 1):
        dp[i][j] += dp[i - 1][j]

        for k in range(1, mp[i] + 1):
            if j - k > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD

for i in range(s, b + 1):
    res = (res + dp[t][i]) % MOD

print(res)

