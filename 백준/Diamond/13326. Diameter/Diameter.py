import math
import sys

def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write("{:.100f}".format(val))
def dist(u, v):
    return (x[u] - x[v]) ** 2 + (y[u] - y[v]) ** 2

n = int(input())
x, y = [], []
arr = [0] * n
li = [0] * n

res = float('inf');pf = 0;s, e = 0, 0

for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    arr[i] = i

for i in range(n):
    for j in range(n):
        if dist(s, e) < dist(i, j):
            s, e = i, j

arr.sort(key=lambda u: dist(s, u))

for i in range(n - 1, -1, -1):
    li[i] = li[i + 1] if i + 1 < n else 0
    for j in range(n - 1, i, -1):
        li[i] = max(li[i], dist(arr[i], arr[j]))

for i in range(n):
    for j in range(i):
        pf = max(pf, dist(arr[i - 1], arr[j]))
    res = min(res, math.sqrt(pf) + math.sqrt(li[i]))

print(res)
