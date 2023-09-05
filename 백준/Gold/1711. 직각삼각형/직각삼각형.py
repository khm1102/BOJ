import math
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(points, i):
    ret = 0
    mp = defaultdict(int)
    tmp = points.copy()
    tmp[0], tmp[i] = tmp[i], tmp[0]
    
    for j in range(1, len(points)):
        x = tmp[j][0] - tmp[0][0]
        y = tmp[j][1] - tmp[0][1]
        g = gcd(x, y)
        if g < 0:
            g = -g
        x //= g
        y //= g
        mp[(x, y)] += 1
    
    for k, v in mp.items():
        cx, cy = k
        if (-cy, cx) in mp:
            ret += v * mp[(-cy, cx)]
    
    return ret

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    ans = 0
    for i in range(n):
        ans += solve(points, i)
    
    print(ans)

if __name__ == '__main__':
    main()
