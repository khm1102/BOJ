def gauss(matrix):
    n = len(matrix)
    for i in range(n):
        div = matrix[i][i];
        for j in range(i, n + 1):matrix[i][j] /= div
        for j in range(n):
            if i == j:continue
            div = -matrix[j][i]
            for k in range(n + 1):matrix[j][k] += matrix[i][k] * div
    return [row[n] for row in matrix]
arr = []
[arr.append(list(map(float,input().split()))) for i in range(int(input()))]
res = (gauss(arr))
print(*[f'{i:.0f}'for i in res])