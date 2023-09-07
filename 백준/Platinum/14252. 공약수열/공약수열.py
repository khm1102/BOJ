import math


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = b, a % b
    return b

def is_coprime(a, b):
    for i in range(a + 1, b):
        if gcd(a, i) == 1 and gcd(i, b) == 1:
            return True
    return False

def f(n, num):
    num.sort()
    cnt = 0
    for i in range(1, n):
        if gcd(num[i], num[i - 1]) != 1:
            cnt += 1 if is_coprime(num[i - 1], num[i]) else 2
    return cnt

n = int(input())
num = list(map(int, input().split()))
print(f(n, num))

