MOD = 1_000_003


n, start, end, late = map(int, input().split())
start, end = start - 1, end - 1
matrix = [[0] * n * 5 for _ in range(n * 5)]

for i in range(n):
    for j in range(1, 5):
        matrix[i * 5 + j][i * 5 + j - 1] = 1
    for j, dis in enumerate(map(int, input())):
        if dis:
            matrix[i * 5][j * 5 + dis - 1] = 1

def mat_mul(m1, m2):
    return [[sum(a * b % MOD for a, b in zip(row1, col2)) % MOD for col2 in zip(*m2)] for row1 in m1]

def mat_pow(m, p):
    if p == 1:
        return m
    if p % 2:
        return mat_mul(m, mat_pow(m, p - 1))
    h = mat_pow(m, p // 2)
    return mat_mul(h, h)

print(mat_pow(matrix, late)[start * 5][end * 5])

