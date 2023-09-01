b2d = lambda n, b: sum((int(x, 36) if x.isalpha() else int(x)) * (b ** i) for i, x in enumerate(n[::-1]))
N, B = input().split()
B = int(B)
print(b2d(N, B))