n, m = map(int, input().split())
arr = set(input() for _ in range(n))
print(sum(1 for _ in range(m) if input() in arr))