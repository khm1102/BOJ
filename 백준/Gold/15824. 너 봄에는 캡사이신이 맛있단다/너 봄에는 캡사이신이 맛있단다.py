MOD = 10 ** 9 + 7


N = int(input().strip())
v = sorted(map(int, input().strip().split()))
print(sum(v[i] * (pow(2, i, MOD) - pow(2, N - i - 1, MOD)) % MOD for i in range(N)) % MOD)


