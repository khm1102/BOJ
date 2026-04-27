n = int(input())
ary = [0] * 10

cur = n
expr = 1
while cur:
    idx = cur % 10
    next_val = cur // 10

    ary[0] += next_val * expr

    for i in range(1, idx + 1):
        ary[i] += (next_val + 1) * expr

    ary[idx] -= expr - (n % expr) - 1

    for i in range(idx + 1, 10):
        ary[i] += next_val * expr

    cur = next_val
    expr *= 10

for i in range(10):
    print(ary[i], end=' ')
