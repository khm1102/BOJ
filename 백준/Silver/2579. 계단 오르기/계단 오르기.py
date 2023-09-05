N = int(input())

arr = [0] * (N + 1)
DP = [0] * (N + 1)

for i in range(1, N + 1):
    arr[i] = int(input())

DP[1] = arr[1]

if N >= 2:
    DP[2] = arr[1] + arr[2]

for i in range(3, N + 1):
    DP[i] = max(DP[i - 2], DP[i - 3] + arr[i - 1]) + arr[i]

print(DP[N])
