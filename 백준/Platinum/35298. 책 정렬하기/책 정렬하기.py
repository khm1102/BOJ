def op(x):
    res.append(x)
    i = x - 1
    arr[:] = [arr[i], arr[i + 1]] + arr[:i] + arr[i + 2:]


n = int(input())
arr = list(map(int, input().split()))
res = []

if sum(1 for i in range(n) for j in range(i + 1, n) if arr[i] > arr[j]) % 2 == 1:
    print("NO")
    exit()

for i in range(n, 2, -1):
    if arr[i - 1] == i:
        continue

    p = arr.index(i) + 1
    if i % 2 == 1:
        if p != 1:
            op(p)
        for _ in range((i - 1) // 2):
            op(i - 1)
    else:
        if p == 1:
            op(2)
            op(2)
        elif p >= 3:
            op(p - 1)
        for _ in range((i - 2) // 2):
            op(i - 1)

print("YES")
print(len(res))
if res: print(*res)
