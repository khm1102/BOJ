import heapq
import sys

class N:
    def __init__(self, v, w, c):
        self.v = v
        self.w = w
        self.c = c
    
    def __lt__(self, o):
        return self.w < o.w

n, m, k = map(int, sys.stdin.readline().split())
s, d = map(int, sys.stdin.readline().split())

a = [[] for _ in range(n + 1)]
dp = [[float('inf')] * n for _ in range(n + 1)]

for _ in range(m):
    x, y, w = map(int, sys.stdin.readline().split())
    a[x].append(N(y, w, 0))
    a[y].append(N(x, w, 0))

for i in range(1, n + 1):
    dp[i] = [float('inf')] * n

h = []
heapq.heappush(h, N(s, 0, 0))

while h:
    t = heapq.heappop(h)
    if t.c + 1 == n:
        continue
    if t.w > dp[t.v][t.c]:
        continue
    for nx in a[t.v]:
        for i in range(1, t.c + 1):
            if dp[nx.v][i] < t.w + nx.w:
                break
        else:
            if dp[nx.v][t.c + 1] > t.w + nx.w:
                dp[nx.v][t.c + 1] = t.w + nx.w
                heapq.heappush(h, N(nx.v, t.w + nx.w, t.c + 1))

r = float('inf')
for i in range(1, n):
    r = min(r, dp[d][i])

sys.stdout.write(str(r) + '\n')

def t(p):
    r = float('inf')
    for i in range(1, n):
        if dp[d][i] == float('inf'):
            continue
        dp[d][i] += i * p
        r = min(r, dp[d][i])
    return r

for _ in range(k):
    p = int(sys.stdin.readline())
    sys.stdout.write(str(t(p)) + '\n')
