def mss(N):
    dp = [0] + [100000] * N

    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[N]

if __name__ == "__main__":
    N = int(input())
    result = mss(N)
    print(result)