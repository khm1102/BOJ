from sys import stdin
from collections import deque

def input():
    return stdin.readline();

def solve(n,k):
    deq = deque(range(1,n+1));
    arr = [];

    while deq:
        for _ in range(k-1):
            deq.append(deq.popleft());
        arr.append(deq.popleft());
    return arr;

n,k = map(int,input().split());
print(f"<{', '.join(map(str, solve(n,k)))}>");