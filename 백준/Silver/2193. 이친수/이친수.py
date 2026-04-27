def solve(N):
    if N == 1 or N == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, N + 1):
        a, b = b, a + b
    return b
print(solve(int(input())))