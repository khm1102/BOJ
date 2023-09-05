def count_sum_combinations(N, K):
    
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    
    for i in range(K + 1):
        dp[i][0] = 1

    for i in range(1, K + 1):
        for j in range(1, N + 1):
            
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

    return dp[K][N]


N, K = map(int, input().split())


result = count_sum_combinations(N, K)
print(result)
