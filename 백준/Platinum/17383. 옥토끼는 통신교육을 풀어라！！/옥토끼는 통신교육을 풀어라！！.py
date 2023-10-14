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
def print(val):return sys.stdout.write(str(val))


n = int(input())
t = list(map(int, input().split()))
t.sort()

def f(rt):
    cnt = 0
    for i in range(n):
        cnt += 1 - (t[i] - 1) // rt
    return cnt > 0

l, h = 1, t[-1]

while l < h:
    mid = (l + h) // 2
    if not f(mid):
        l = mid + 1
    else:h = mid

print(h)