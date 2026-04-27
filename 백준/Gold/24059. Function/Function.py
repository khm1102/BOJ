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


def main():
    n = int(input())
    li = list(map(int, input().split()))
    k = int(input())

    if n == 0:
        print(li[0] % k)
    elif n == 1:
        answer = li[0]
        answer = pow(li[1], answer, k)
        print(answer)
    else:
        temp = li[0]
        temp = pow(li[1], temp, k - 1)
        temp += k - 1

        answer = li[2]
        answer = pow(answer, temp, k)

        print(answer)


if __name__ == "__main__":
    main()

