n = int(input())
d = [0, 0]

for i in range(2, n + 1):
    d.append(min(d[i - 1], d[i // 2] if i % 2 == 0 else float('inf'), d[i // 3] if i % 3 == 0 else float('inf')) + 1)

print(d[n])
