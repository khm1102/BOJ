E, S, M = map(int, input().split())
year = 1
while (year - E) % 15 or (year - S) % 28 or (year - M) % 19: year += 1
print(year)