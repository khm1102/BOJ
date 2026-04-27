from heapq import heappush, heapreplace

def solve(l:list):
    l.sort();h =[]

    for i,j in l: heapreplace(h, j) if h and h[0] <= i else heappush(h,j)
    return len(h)

print(solve([list(map(int,input().split())) for _ in range(int(input()))]))