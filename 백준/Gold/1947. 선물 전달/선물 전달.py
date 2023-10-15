MOD = 1000000000 

def f(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 0
    for i in range(2, N + 1):
        dp[i] = ((dp[i - 1] + dp[i - 2]) % MOD) * (i - 1) % MOD
    return dp[N]

N = int(input())
result = f(N)
print(result)
