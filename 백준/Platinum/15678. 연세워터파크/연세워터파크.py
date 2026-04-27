# 참고 하고 품
from collections import deque

N, D = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * N
q = deque()

for i in range(N):
    dp[i] = a[i]
    while q and q[0][0] < i - D:
        q.popleft()
    if q:
        dp[i] = max(dp[i], q[0][1] + a[i])
    while q and q[-1][1] < dp[i]:
        q.pop()
    q.append((i, dp[i]))

print(max(dp))
