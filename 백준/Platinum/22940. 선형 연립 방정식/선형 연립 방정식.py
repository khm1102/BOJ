def gauss_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        div = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= div
        
        for j in range(n):
            if i == j:
                continue
            div = -matrix[j][i]
            for k in range(n + 1):
                matrix[j][k] += matrix[i][k] * div
    
    result = [row[n] for row in matrix]
    return result

def main():
    n = int(input())
    matrix = []
    
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    result = gauss_elimination(matrix)
    
    for i in result:
        print(f'{i:.0f}', end=' ')

if __name__ == "__main__":
    main()
