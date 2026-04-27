import heapq
import sys

class Node:
    def __init__(self, v, w, c):
        self.v = v
        self.w = w
        self.c = c
    
    def __lt__(self, other):
        return self.w < other.w

N, M, K = map(int, input().split())
S, D = map(int, input().split())

arr = [[] for _ in range(N + 1)]
dp = [[float('inf')] * N for _ in range(N + 1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    arr[a].append(Node(b, w, 0))
    arr[b].append(Node(a, w, 0))

for i in range(1, N + 1):
    dp[i] = [float('inf')] * N

heap = []
heapq.heappush(heap, Node(S, 0, 0))

while heap:
    temp = heapq.heappop(heap)
    if temp.c + 1 == N:
        continue
    if temp.w > dp[temp.v][temp.c]:
        continue
    for next_node in arr[temp.v]:
        for i in range(1, temp.c + 1):
            if dp[next_node.v][i] < temp.w + next_node.w:
                break
        else:
            if dp[next_node.v][temp.c + 1] > temp.w + next_node.w:
                dp[next_node.v][temp.c + 1] = temp.w + next_node.w
                heapq.heappush(heap, Node(next_node.v, temp.w + next_node.w, temp.c + 1))

result = float('inf')
for i in range(1, N):
    result = min(result, dp[D][i])

print(result)

def tax(p):
    result = float('inf')
    for i in range(1, N):
        if dp[D][i] == float('inf'):
            continue
        dp[D][i] += i * p
        result = min(result, dp[D][i])
    return result

for _ in range(K):
    p = int(input())
    print(tax(p))
