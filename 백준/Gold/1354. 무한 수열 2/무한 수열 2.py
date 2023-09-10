a, b, c, d, e = map(int, input().split());f = {}
solve = lambda i: 1 if i <= 0 else f[i] if i in f else f.setdefault(i, solve(i // b - d) + solve(i // c - e))
print(solve(a))