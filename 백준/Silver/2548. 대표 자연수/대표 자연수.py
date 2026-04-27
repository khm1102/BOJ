def solve(n):
    n.sort()
    return n[(len(n) - 1) // 2]
input()
print(solve(list(map(int, input().split()))))