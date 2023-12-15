n, m, k = map(int, input().split())

if n + 1 < m + k or n > m * k:
    print(-1)
    exit()

arr = list(range(1, n + 1))
temp = 0
for i in range(m):
    e = min(temp + k, n - m + i + 1)
    arr[temp:e] = reversed(arr[temp:e])
    temp = e

print(*arr)
