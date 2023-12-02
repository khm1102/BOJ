from collections import deque
import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))


n = int(input())
S = deque()
ans = 0

for _ in range(n):
    h = int(input())
    cnt = 1
    while S and S[-1][0] <= h:
        ans += S[-1][1]
        if S[-1][0] == h:
            cnt += S[-1][1]
        S.pop()
    if S:
        ans += 1
    S.append((h, cnt))

print(ans)
