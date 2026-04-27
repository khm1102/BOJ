from sys import stdin

def input():
    return stdin.readline()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

tree = [0] * (n + 1)
res = 0

for i, x in enumerate(arr, 1):
    temp = 0
    y = x
    while y > 0:
        temp += tree[y]
        y -= y & -y
    res += i - 1 - temp
    while x <= n:
        tree[x] += 1
        x += x & -x

print(min(m + res, n * (n - 1) // 2))
