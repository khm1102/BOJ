def multiply_matrix(a, b):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007]
    ]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return multiply_matrix(half_power, half_power)
    else:
        half_power = matrix_power(matrix, (n - 1) // 2)
        return multiply_matrix(matrix, multiply_matrix(half_power, half_power))

def fibonacci(n):
    if n <= 1:
        return n

    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0][0]

n = int(input())

result = fibonacci(n)
print(result)
