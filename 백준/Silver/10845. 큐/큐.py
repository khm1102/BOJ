from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
N = int(input())
for _ in range(N):
    k = input().split()
    if k[0] == 'push':
        queue.append(int(k[1]))
    elif k[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif k[0] == 'size':
        print(len(queue))
    elif k[0] == 'empty':
        print(0 if queue else 1)
    elif k[0] == 'front':
        print(queue[0] if queue else -1)
    elif k[0] == 'back':
        print(queue[-1] if queue else -1)