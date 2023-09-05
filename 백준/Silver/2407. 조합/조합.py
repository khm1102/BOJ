import math

n, m = map(int, input().split())
result = math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
print(result)