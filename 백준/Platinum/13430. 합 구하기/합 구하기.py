MOD = 10**9 + 7

def matrix_multiply(A, B):
    return [[sum(a * b % MOD for a, b in zip(row_a, col_b)) % MOD for col_b in zip(*B)] for row_a in A]

k, n = map(int, input().split())

ans = [[i == j for j in range(k + 2)] for i in range(k + 2)]
arr = [[j <= i for j in range(k + 2)] for i in range(k + 2)]

n -= 1

while n > 0:
    if n % 2 == 1:
        ans = matrix_multiply(ans, arr)
    arr = matrix_multiply(arr, arr)
    n //= 2

print(sum(ans[k + 1]) % MOD)

