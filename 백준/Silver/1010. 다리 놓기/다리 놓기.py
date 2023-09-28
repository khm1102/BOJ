import math
f = lambda n, k: math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
T = int(input())
print(*[f(M, N) for _ in range(T) for N, M in [map(int, input().split())]])