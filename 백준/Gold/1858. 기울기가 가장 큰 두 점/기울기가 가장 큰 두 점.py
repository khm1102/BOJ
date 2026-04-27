def solve(left, right):
    x = right[0] - left[0]
    y = right[1] - left[1]
    return abs(y / x)

n = int(input())
arr = [tuple(map(int, input().split())) + (i,) for i in range(n)]
arr.sort(key=lambda x: x[0])

val = -1
temp = float('inf')

for i in range(n - 1):
    tmp_tan = solve(arr[i], arr[i + 1])
    if val < tmp_tan:
        val = tmp_tan
        temp = min(arr[i][2], arr[i + 1][2])
    elif val == tmp_tan:
        temp = min(temp, min(arr[i][2], arr[i + 1][2]))

arr.sort(key=lambda x: x[2])

kl = float('inf')
for i in range(temp + 1, n):
    tmp_tan = solve(arr[temp], arr[i])
    if val == tmp_tan:
        kl = i
        break


print(temp + 1, kl + 1)
