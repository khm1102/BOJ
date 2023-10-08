import sys
import os
import math
import cmath
import decimal
import itertools
import heapq
from bisect import bisect_left, bisect_right
from collections import deque


def input(): return sys.stdin.readline().strip()


def print(val): return sys.stdout.write(str(val))


n = int(input())
ck = [[False] * 101 for _ in range(101)]
dp = [[0] * 101 for _ in range(101)]

for _ in range(n):
    u, v = map(int, input().split())
    ck[u][v] = ck[v][u] = True
    dp[u][v] = dp[v][u] = 1

for i in range(2, 101):
    for j in range(1, 101 - i):
        q = j + i
        for k in range(j, q):
            dp[j][q] = max(dp[j][q], ck[j][q] + dp[j][k] + dp[k + 1][q])

print(dp[1][100])


