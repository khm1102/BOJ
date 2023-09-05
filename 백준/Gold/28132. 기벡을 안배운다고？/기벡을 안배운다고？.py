from collections import defaultdict
from math import gcd
N = int(input().strip())
vec_map = defaultdict(int)
zero_vecs = 0
total = 0
for _ in range(N):
    x, y = map(int, input().strip().split())
    if x == 0 and y == 0:
        zero_vecs += 1
        continue
    g = gcd(x, y)
    x //= g
    y //= g
    if x < 0 or (x == 0 and y < 0):
        x, y = -x, -y
    total += vec_map[(y, -x)] + vec_map[(-y, x)]
    vec_map[(x, y)] += 1
total += zero_vecs * (N - zero_vecs) + (zero_vecs * (zero_vecs - 1)) // 2

print(total)
