import sys
from bisect import bisect_left

def solve():
    n = int(input())
    lines = sorted([tuple(map(int, input().split())) for _ in range(n)])
    dp, trace = [], [-1] * n

    for i, (_, b) in enumerate(lines):
        if not dp or dp[-1][1] < b:
            if dp:
                trace[i] = dp[-1][0]
            dp.append((i, b))
        else:
            idx = bisect_left([b for _, b in dp], b)
            dp[idx] = (i, b)
            if idx > 0:
                trace[i] = dp[idx - 1][0]

    lis_set = set()
    i = dp[-1][0]
    while i >= 0:
        lis_set.add(i)
        i = trace[i]

    print(n - len(dp))
    for i, (a, _) in enumerate(lines):
        if i not in lis_set:
            print(a)

solve()
