n = int(input())
arr = list(map(int, input().split()))

res = []
for i in range(n, 0, -1):
    res.insert(arr[i-1], i)

print(*res)
