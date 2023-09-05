import heapq
import sys

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
pque = []

for _ in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(pque, (abs(x), x))
    else:
        output(f"{heapq.heappop(pque)[1]}\n" if pque else "0\n")
