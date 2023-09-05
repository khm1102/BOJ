n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
results = []

calculate_result = lambda a, b: (
    10 if a == 0 else
    a if a in (1, 5, 6) else
    (a**2) % 10 if a in (4, 9) and b % 2 == 0 else
    a % 10 if a in (4, 9) and b % 2 != 0 else
    (a**b) % 10 if a in (2, 3, 7, 8) else 0
)

for a, b in arr:
    a %= 10
    result = calculate_result(a, b)
    results.append(result)

for result in results:
    print(result)
