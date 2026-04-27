import sys
input = sys.stdin.readline

def solve(n, m):
    if n == 1 or m == 1:
        return "First"

    if n == 2 or m == 2:
        return "First"

    if n % 2 == 1 and m % 2 == 1:
        return "First"

    if n % 2 == 0 and m % 2 == 0:
        return "Second"

    return "Second"

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(solve(n,m))