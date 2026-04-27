from sys import stdin, stdout, maxsize
from heapq import heappush, heappop

def input():return stdin.readline().strip()

def print(s): stdout.write(str(s) + "\n")

def next_start(nt, ng):
    return nt if nt % ng == 0 else (nt // ng + 1) * ng

def solve(n, k, arr):
    inf = maxsize
    
    pq = []
    t = [[inf] * (n + 1) for _ in range(k + 1)]

    heappush(pq, (0, 1, 0))
    t[0][1] = 0

    while pq:
        nt, nn, nk = heappop(pq)

        if nt > t[nk][nn]:
            continue

        if nn == n:
            return nt

        for e, et, g in arr[nn]:
            ns = next_start(nt, g)

            if ns + et < t[nk][e]:
                heappush(pq, (ns + et, e, nk))
                t[nk][e] = ns + et

            if nk < k and nt + et < t[nk + 1][e] and nt + et < t[nk][e]:
                heappush(pq, (nt + et, e, nk + 1))
                t[nk + 1][e] = nt + et

    return -1

n, m, k = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, t, g = map(int, input().split())
    arr[u].append((v, t, g))

print(solve(n, k, arr))
