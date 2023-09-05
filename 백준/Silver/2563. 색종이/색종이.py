a = [[0] * 100 for _ in range(100)]
cnt = 0

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if not a[i][j]:
                cnt += 1
                a[i][j] = 1

print(cnt)

