import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
mod = 1e18;b = 0;v = True;m = 0

for _ in range(int(input())):
    n,k = map(int, input().split())
    if b + n < 0:
        temp = k - n - b
        mod = min(mod, k) if k != 0 else mod
        m = temp if m == 0 else gcd(m, temp)

        if m <= mod and mod != 1e18:
            v = False
            break
    else:
        if b + n != k:
            v = False
            break
    b = k

print(m if v and m != 0 else "1" if v else "-1")