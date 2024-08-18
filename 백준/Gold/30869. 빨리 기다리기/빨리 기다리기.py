import heapq
import sys

def input():
    return sys.stdin.readline().strip()

inf = sys.maxsize

def get_next_start(now_t, next_g):
    if now_t == 0:
        return 0
    p = now_t // next_g
    q = now_t % next_g
    return now_t if q == 0 else next_g * (p + 1)

def dijkstra(n, k, edge_list):
    pq = []
    t = [[inf] * (n + 1) for _ in range(k + 1)]
    
    heapq.heappush(pq, (0, 1, 0))
    t[0][1] = 0

    while pq:
        now_t, now_n, now_k = heapq.heappop(pq)

        if now_t > t[now_k][now_n]:
            continue
        if now_n == n:
            return now_t

        for e, edge_t, g in edge_list[now_n]:
            next_start = get_next_start(now_t, g)

            if next_start + edge_t < t[now_k][e]:
                heapq.heappush(pq, (next_start + edge_t, e, now_k))
                t[now_k][e] = next_start + edge_t

            if now_k < k and now_t + edge_t < t[now_k + 1][e] and now_t + edge_t < t[now_k][e]:
                heapq.heappush(pq, (now_t + edge_t, e, now_k + 1))
                t[now_k + 1][e] = now_t + edge_t

    return -1

n, m, k = map(int, input().split())
edge_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, t, g = map(int, input().split())
    edge_list[u].append((v, t, g))

print(dijkstra(n, k, edge_list))
