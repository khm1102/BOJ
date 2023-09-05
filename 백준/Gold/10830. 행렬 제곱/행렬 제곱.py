def multiply_matrix(a, b, mod):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= mod
    return result

def matrix_power(matrix, exp, mod):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1

    while exp > 0:
        if exp % 2 == 1:
            result = multiply_matrix(result, matrix, mod)
        matrix = multiply_matrix(matrix, matrix, mod)
        exp //= 2

    return result

if __name__ == "__main__":
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = matrix_power(A, B, 1000)

    for row in result:
        print(' '.join(map(str, row)))
