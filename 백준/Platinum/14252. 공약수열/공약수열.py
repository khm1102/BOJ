import math

def gcd(x, y):
    x1 = max(x, y)
    y1 = min(x, y)
    while x1 % y1 != 0:
        tmp = y1
        y1 = x1 % y1
        x1 = tmp
    return y1

def chk(a, b):
    for i in range(a + 1, b):
        if gcd(a, i) == 1 and gcd(i, b) == 1:
            return 1
    return 2


n = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0
for i in range(1, n):
    if gcd(num[i], num[i - 1]) != 1:
        cnt += chk(num[i - 1], num[i])
print(cnt)

