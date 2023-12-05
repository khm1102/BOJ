mod = 10 ** 9 + 7

def add(a, b):
    return (a + b) % mod

def s(a, b):
    return (a - b + mod) % mod

def c_dp(n, m):
    dp = [0] * (1 << m)
def p_mod(x, n):
    return pow(x, n, mod)

def c_dp(n, m):
    dp = [0] * (1 << m)

    for _ in range(n):
        t, *val = map(int, input().split())
        dp[sum(1 << (val - 1) for val in val)] += 1

    for i in range(m):
        for ma in range(1 << m):
            if ma & (1 << i):
                dp[ma] = add(dp[ma], dp[ma ^ (1 << i)])

    for i in range(1 << (m - 1)):
        dp[i], dp[i ^ ((1 << m) - 1)] = dp[i ^ ((1 << m) - 1)], dp[i]

    for i in range(1 << m):
        dp[i] = p_mod(2, dp[i])

    return dp


n, m = map(int, input().split())
dp = c_dp(n, m)
print(sum(dp[i] if bin(i).count('1') % 2 == 0 else -dp[i] for i in range(1 << m)) % mod)