import math
n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
x = sum(point[0] for point in p) / n
y = sum(point[1] for point in p) / n
a, b, w, s = x, y, 0.1, float('inf')
o = lambda x, y: x ** 2 + y ** 2
for _ in range(10000):
    m,v=max(((i, o(a - x, b - y)) for i,(x, y) in enumerate(p)), key=lambda x:x[1])
    if v<s:s=v
    a+=(p[m][0]-a)*w
    b+=(p[m][1]-b)*w
    w*=0.995
print(f"{a:.3f} {b:.3f}\n{math.sqrt(s):.3f}")