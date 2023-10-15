h, w = map(int, input().split())
ans = -1
arr = []

for _ in range(h):arr.append(input())
k = int(input())
for i in range(h):
    z = arr[i].count('0')
    sum = 0
    if z <= k and z % 2 == k % 2:
        for y in range(h):
            if arr[i] == arr[y]:
                sum += 1
    ans = max(sum, ans)
print(ans)