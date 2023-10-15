import sys
d1, d2, x = map(int, sys.stdin.readline().split())
if d1 > d2:d1, d2 = d2, d1
p = (100 - x) / x
print("{:.6f}".format((p + 1) / (p * d2 / d1 + 1) * d2))