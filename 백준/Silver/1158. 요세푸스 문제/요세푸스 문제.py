from collections import deque

def solved(n,k):
    queue = deque(range(1,n+1))
    sequence = []

    while queue:
        for _ in range(k-1):
            queue.append(queue.popleft())
        sequence.append(queue.popleft())
    return sequence



n,k = map(int,input().split())
res = solved(n,k)

print(f"<{', '.join(map(str, res))}>")
