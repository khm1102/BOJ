import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))
n = int(input())
s = [0] * (n + 1)

for i in range(2, n + 1):
    a = set()
    for j in range(1, i):
        a.add(s[j - 1] ^ s[i - 1 - j])

    while s[i] in a:
        s[i] += 1

print(1 if s[n] else 2)
