def matrix_operations(N, M, Q, operations):
    matrix = [[0] * M for _ in range(N)]
    row_sum = [0] * N
    col_sum = [0] * M

    for op in operations:
        if op[0] == 1:
            r, v = op[1], op[2]
            row_sum[r - 1] += v
        else:
            c, v = op[1], op[2]
            col_sum[c - 1] += v
    
    for i in range(N):
        for j in range(M):
            matrix[i][j] = row_sum[i] + col_sum[j]

    return matrix


N, M, Q = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(Q)]

result_matrix = matrix_operations(N, M, Q, operations)

for row in result_matrix:
    print(*row)
