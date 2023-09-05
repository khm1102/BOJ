import sys
import heapq

N = int(sys.stdin.readline())


heap = []

for _ in range(N):
    x = int(sys.stdin.readline()) 

    if x == 0:
        if not heap:
            print(0)
        else:
            max_value = -heapq.heappop(heap)
            print(max_value)
    else:
        heapq.heappush(heap, -x)
