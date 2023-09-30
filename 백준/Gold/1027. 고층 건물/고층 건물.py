n = int(input())
b = list(map(int, input().split()))

cnt = [0] * n
for i in range(n):
    mg = -1000000000
    for j in range(i + 1, n):
        h = b[j] - b[i]
        w = j - i
        g = h * 1.0 / w
        if g <= mg:
            continue
        mg = g
        cnt[i] += 1
        cnt[j] += 1
print(max(cnt))
