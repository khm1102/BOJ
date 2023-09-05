def r(matrix, row):
    matrix[row].insert(0, matrix[row].pop())

def rotate(matrix):
    return [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix[0]))]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        r(matrix, op[1] - 1)
    elif op[0] == 2:
        matrix = rotate(matrix)

for row in matrix:
    print(*row)
