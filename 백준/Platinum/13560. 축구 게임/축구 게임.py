import sys
def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))

n, m = int(input()), sorted(map(int, input().split()))

temp = 0
for i in range(n):
    temp += m[i]
    if temp < i * (i + 1) // 2:
        print(-1)
        exit()

print(1 if temp == n * (n - 1) // 2 else -1)
