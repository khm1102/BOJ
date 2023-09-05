def find(triangle):
    n = len(triangle)

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]  

n = int(input()) 
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

print(find(triangle))
