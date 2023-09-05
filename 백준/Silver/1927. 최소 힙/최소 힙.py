import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:
            sys.stdout.write(str(heapq.heappop(heap)) + "\n")
        else:
            sys.stdout.write("0\n")
    else:
        heapq.heappush(heap, x)
