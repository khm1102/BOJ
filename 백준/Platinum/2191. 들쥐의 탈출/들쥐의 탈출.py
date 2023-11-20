import sys
def input(): return sys.stdin.readline().strip()

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def f(x):
    global p, vi
    for nx in g[x]:
        if vi[nx]:
            continue
        vi[nx] = 1
        if p[nx] == -1 or f(p[nx]):
            p[nx] = x
            return 1
    return 0

n, m, s, v = map(int, input().split())
a = [list(map(float, input().split())) for _ in range(n)]
h = [list(map(float, input().split())) for _ in range(m)]
g = [[] for _ in range(n + 1)]
p = [-1] * (m + 1)
ans = n

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if dist(a[i - 1], h[j - 1]) <= s ** 2 * v ** 2:
            g[i].append(j)

for i in range(1, n + 1):
    vi = [0] * (m + 1)
    ans -= f(i)

print(ans)
