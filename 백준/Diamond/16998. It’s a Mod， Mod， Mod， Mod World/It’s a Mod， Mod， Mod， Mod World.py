import sys
from math import gcd
def input():
    return sys.stdin.readline().strip()
def mod(p, q, n):
    if p == 0:
        return 0
    if p >= q:
        return n * (n + 1) // 2 * (p // q) + mod(p % q, q, n)
    return n * (p * n // q) + n // q - mod(q, p, p * n // q)

for _ in range(int(input())):
    p, q, n = map(int, input().split())
    r = gcd(p, q)
    print(n * (n + 1) // 2 * p - q * mod(p // r, q // r, n))

