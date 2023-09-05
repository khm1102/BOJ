import heapq

def min_rooms(sch):
    if not sch:
        return 0

    sch.sort(key=lambda x: x[0])
    rooms = []

    heapq.heappush(rooms, sch[0][1])

    for i in range(1, len(sch)):
        if sch[i][0] >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, sch[i][1])

    return len(rooms)

N = int(input())
sch = []
for _ in range(N):
    S, T = map(int, input().split())
    sch.append((S, T))

result = min_rooms(sch)
print(result)
