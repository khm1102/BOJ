import sys
def input(): return sys.stdin.readline().strip()
def print(s):return sys.stdout.write(s)

for _ in range(int(input())):
    p, m, f, c = map(int,input().split())

    n = (m // p) + ((m // p) * c) // f
    d = (m // p)
    res = (m // p) * c
    if res >= f:
        d += (res - f) // (f - c) + 1
    print(str(d - n) + "\n")