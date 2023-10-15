import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))

a, b = map(lambda x: max(x, 3), map(int, input().split()))
a, b = (a + 1) if a % 2 else a, (b - 1) if b % 2 else b
a, b = a // 2, b // 2
print((b * (b + 1) - a * (a - 1)) if a <= b else 0)