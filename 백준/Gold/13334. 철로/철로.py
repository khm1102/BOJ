import heapq

n = int(input())
inputQ = []

for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        inputQ.append((o, h))
    else:
        inputQ.append((h, o))

d = int(input())


inputQ.sort(key=lambda x: (x[1], x[0]))

maxSize = 0
pq = []

for i in range(len(inputQ)):
    iR = inputQ[i][1]
    iL = inputQ[i][0]

    if iR - iL <= d:
        heapq.heappush(pq, iL)
    else:
        continue

    while pq:

        tmp = pq[0]
        if iR - tmp <= d:
            break
        else:
            heapq.heappop(pq)

    maxSize = max(maxSize, len(pq))

print(maxSize)
