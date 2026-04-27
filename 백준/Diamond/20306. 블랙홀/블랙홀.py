from sys import stdin

def input():
    return stdin.readline()

def ccw(a, b, c):
    return a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - a[1]*b[0] - b[1]*c[0] - c[1]*a[0] >= 0

def find(i, la, lb, ra, rb, vectors):
    low, high = 0, 10**19
    while low <= high:
        mid = (low + high) // 2
        l = [la * (mid + 1), lb * (mid + 1)]
        r = [ra * (mid + 1), rb * (mid + 1)]
        if ccw(l, r, vectors[i][0]):
            high = mid - 1
        else:
            low = mid + 1
    return low

n, m, k = map(int, input().split())
point_a, point_y = map(int, input().split())

vectors, temp, cnt = [], [], []

for _ in range(n + m):
    x, y, typ = *map(int, input().split()), 1 if _ < n else 0
    vector = [x - point_a, y - point_y]
    vectors.append([vector, typ])
    if typ: temp.append(vector)

sort_key = lambda x: (x[0] <= 0, x[1] / x[0] if x[0] != 0 else float('inf'))
vectors.sort(key=lambda x: sort_key(x[0]))
temp.sort(key=sort_key)

res = n - 1
for i, (vec, typ) in enumerate(vectors):
    if typ:
        res = (res + 1) % n
        continue
    cnt.append(find(i, *temp[res], *temp[(res + 1) % n], vectors))

print(sorted(cnt)[k - 1])
