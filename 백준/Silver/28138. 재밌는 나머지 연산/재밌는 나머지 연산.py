def solve(N, R):
    total = 0
    limit = int((N - R)**0.5)
    for m in range(1, limit+1):
        if (N-R) % m == 0:
            if m > R:
                total += m
            if (N-R) // m > R and m * m != N - R:
                total += (N-R) // m
    return total

N, R = map(int,input().split())
print(solve(N, R))
